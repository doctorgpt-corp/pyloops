# Install dependencies
install:
    uv sync --all-groups

# Run linting
lint:
    uv run ruff check src/

# Format code
fmt:
    uv run ruff check --fix src/
    uv run ruff format src/

# Run type checking
typecheck:
    uv run pyright src/

# Run all checks (lint + typecheck)
check: lint typecheck

# Build the package
build:
    uv build

# Bump client version
bump-client:
    #!/usr/bin/env bash
    set -e
    CURRENT=$(grep '^version = ' pyproject.toml | sed 's/version = "\(.*\)"/\1/')

    # Count segments (split by .)
    IFS='.' read -ra PARTS <<< "$CURRENT"
    NUM_PARTS=${#PARTS[@]}

    if [ $NUM_PARTS -eq 3 ]; then
        # No client version yet, add .1
        NEW_VERSION="$CURRENT.1"
    elif [ $NUM_PARTS -eq 4 ]; then
        # Increment existing client version
        MAJOR=${PARTS[0]}
        MINOR=${PARTS[1]}
        PATCH=${PARTS[2]}
        CLIENT=${PARTS[3]}
        NEW_CLIENT=$((CLIENT + 1))
        NEW_VERSION="$MAJOR.$MINOR.$PATCH.$NEW_CLIENT"
    else
        echo "❌ Error: Unexpected version format: $CURRENT"
        exit 1
    fi

    # Update pyproject.toml
    sed -i '' "s/^version = .*/version = \"$NEW_VERSION\"/" pyproject.toml

    # Update lockfile
    uv sync

    echo "✅ Bumped version: $CURRENT → $NEW_VERSION"

# Regenerate SDK from latest OpenAPI spec
generate:
    @echo "🗑️  Removing old generated code..."
    rm -rf src/pyloops/_generated
    @echo "📥 Fetching OpenAPI spec and generating SDK..."
    uv tool run openapi-python-client generate --url https://app.loops.so/openapi.yaml --meta uv
    @echo "📦 Moving generated code..."
    mv loops-open-api-spec-client/loops_open_api_spec_client src/pyloops/_generated
    @echo "🧹 Cleaning up..."
    rm -rf loops-open-api-spec-client openapi.yaml
    @echo "✨ Done! Running checks..."
    just check

# Clean build artifacts
clean:
    rm -rf dist/ build/ *.egg-info .pytest_cache .ruff_cache
