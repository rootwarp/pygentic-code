.PHONY: install lint format typecheck test run

install:
	uv pip install -e ".[dev]"

lint:
	uv run ruff check src/ tests/

format:
	uv run ruff format src/ tests/

typecheck:
	uv run mypy src/

test:
	uv run pytest

run:
	uv run code-agent $(ARGS)
