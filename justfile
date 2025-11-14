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
