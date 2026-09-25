# Install dependencies
install:
    uv sync --all-groups

# Run linting
lint:
    uv run ruff check .

# Format code and tests
format:
    uv run ruff check --fix .
    uv run ruff format .

# Run type checking
typecheck:
    uv run pyright src/

# Run tests
test:
    uv run pytest tests/

# Run all checks (lint + typecheck + tests)
check: lint typecheck test

# Build the package
build:
    uv build

# Regenerate SDK from latest OpenAPI spec
generate:
    @echo "🗑️  Removing old generated code..."
    rm -rf src/pyloops/_generated
    @echo "📥 Fetching OpenAPI spec..."
    curl -fsSL https://app.loops.so/openapi.yaml -o src/pyloops/openapi.yaml
    @echo "⚙️  Generating SDK..."
    uv tool run openapi-python-client generate --path src/pyloops/openapi.yaml --meta uv
    @echo "📦 Moving generated code..."
    mv loops-open-api-spec-client/loops_open_api_spec_client src/pyloops/_generated
    @echo "🧹 Cleaning up..."
    rm -rf loops-open-api-spec-client
    @echo "✨ Done! Running checks..."
    just check

# Clean build artifacts
clean:
    rm -rf dist/ build/ *.egg-info .pytest_cache .ruff_cache
