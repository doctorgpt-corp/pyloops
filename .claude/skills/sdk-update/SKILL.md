---
name: sdk-update
description: Handle an automated "Update SDK to Loops API version X" bot PR - triage the open ones, classify the regenerated diff, repair the hand-written wrapper, and ship it. Use for "handle the bot SDK update PR", "new Loops API version", "update SDK to 1.x.y", or "close superseded update PRs".
---

# SDK update

The bot regenerates `src/pyloops/_generated/` and bumps the version. It never
touches the hand-written layer, so its PR usually cannot merge on its own:
`import pyloops` breaks on a symbol the generator renamed or dropped. Take the
bot's branch, repair the wrapper on top of it, ship both together.

This repo is public and stands alone. Never name a consumer project, internal
service, host or secret store in code, comments, commit messages or PR text.

## 1. Triage the open bot PRs

```bash
gh pr list --state open --search "Update SDK to Loops API version in:title"
```

Keep the newest API version. Close each older one:

```bash
gh pr comment <N> --body "Superseded by #<newest> (Loops API <x.y.z>)."
gh pr close <N> --delete-branch
```

Bot PRs are opened with `GITHUB_TOKEN`, so no workflow runs on them. An absent
or green check list means nothing - `just check` on your machine is the gate.

## 2. Branch

```bash
git fetch origin
git checkout -b sdk-<x.y.z> origin/update-sdk-<x.y.z>
```

The bot's regen commit stays first and untouched; repair commits go on top.
The tree does not import between the regen and the first repair, which is
expected - say so in the PR body and ask for squash or merge, not rebase.

## 3. Classify the diff

Most of the diff is generator churn (StrEnum, `Self`, docstring rewording,
import reordering). Ignore it and hunt for the substantive changes:

| Looking for | Command |
|---|---|
| New or removed endpoints | `git diff --name-status origin/main..HEAD -- src/pyloops/_generated/api/ \| grep -E '^[AD]'` |
| Removed or renamed models | `git diff origin/main..HEAD -- src/pyloops/_generated/models/__init__.py \| grep '^-'` |
| Bodies degraded to raw JSON | `git grep -n "body: Any" src/pyloops/_generated/api/` |
| New required fields | `git diff origin/main..HEAD -- src/pyloops/_generated/models/ \| grep -E '^\+.*d\.pop\("' \| grep -v UNSET` |
| Module renames | compare the `api/` tree listing before and after |

`d.pop("x")` without a default is a required field; `d.pop("x", UNSET)` is
optional. Read the endpoint's `_parse_response` for every status code it now
handles - that is where a new 204 or 409 shows up.

## 4. Repair recipes

- **Module renamed** - mechanical import and call-site fix in `client.py`. Own
  commit, `refactor:`, no behaviour change.
- **Model removed because the schema became a `oneOf`** - the generated
  function takes `body: Any` and sends it raw. Build the dict in the wrapper
  with camelCase keys, send exactly the keys the caller supplied, and validate
  the mutually exclusive arguments before the call rather than letting the API
  answer 400.
- **Success schema degraded to `oneOf` / `allOf`** - no parse branch is
  emitted and `response.parsed` is `None` on success, so `_unwrap` raises on
  every 200. Switch to `_unwrap_raw`, which decodes the body itself. The return
  type widens to `dict[str, Any]`: that is breaking, mark the commit `!`.
- **Empty success body (204)** - neither helper applies. Raise on the failure
  model, then check the status and return `True`.
- **New required field on a response model** - every mock body in `testing.py`
  feeding that model raises `KeyError`. Add the field there and to any fixture
  inlined in a test; assert it in one happy-path test so a future drop fails
  loudly.
- **New endpoint** - one commit carrying all four parts: the `client.py`
  method, a named respx route plus fixture in `testing.py`, the
  `EXPECTED_ROUTE_NAMES` entry with happy-path and error tests, and the row in
  the `CLAUDE.md` named-route table.
- **Changed behaviour on an existing argument** - keep the old spelling
  working behind a `DeprecationWarning` and send the new shape on the wire.
  Never change what an argument means in silence.

## 5. Commit and ship

Conventional Commits, one concern per commit, `!` only when a public return
type changes or a method or argument is removed or renamed (see `CLAUDE.md`).
Retitle the bot PR's non-conventional title on the human PR.

The version stays the bot's three-segment value when regen and repair ship
together. `just bump-client` (the fourth segment) is only for a wrapper-only
release on top of an API version that already shipped.

Open the human PR, then close the bot PR as superseded by it.

## 6. Gate

`just check` must be fully green: `ruff check`, `ruff format --check`,
`pyright src/`, `pytest`. Refresh the test counts in `CLAUDE.md` and confirm
`EXPECTED_ROUTE_NAMES` and the named-route table still agree.

## Known gaps

Mention these where they bite; do not fix them as a side effect of an update.

- `just generate` and `check-updates.yml` both call
  `uv tool run openapi-python-client`, which resolves the newest release. The
  dev-dependency entry is a floor, not a pin, so a local regeneration is not
  guaranteed to reproduce the bot's tree.
- `just bump-client` uses `sed -i ''`, which only works on macOS.
- Bot PRs get no CI run at all.
