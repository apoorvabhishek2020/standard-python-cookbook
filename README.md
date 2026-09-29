# Standard Python Cookbook

Strict, reusable Python quality standards. Copy the files you need into any project.

## What This Gives You

- `ruff` for formatting and linting (strict: `select = ["ALL"]`)
- `mypy` in strict mode
- optional `basedpyright` as a second strict type checker
- `pytest` + `pytest-cov` with mandatory branch coverage
- optional `mutmut` mutation testing
- `pre-commit` local checks
- a single `./runtests` command with clear, ordered, timed terminal output

## Quick Start

1. Copy the files you need (see "Which Files To Copy" below) into your project.
2. Install dependencies:
   ```bash
   uv sync --dev
   ```
3. Scaffold your framework, for example:
   ```bash
   django-admin startproject config .
   ```
   or set up FastAPI/Flask however you normally do.
4. Delete the sample `src/` package included here.
5. Open `quality.toml` and update the paths to match your project. This is the only file you normally need to edit.
6. Run the quality gate:
   ```bash
   ./runtests
   ```

## Which Files To Copy

Core (always copy):

- `pyproject.toml` — dev dependencies (merge into your own if you already have one)
- `quality.toml` — paths and thresholds (the file you edit)
- `runtests` — the quality-gate command
- `quality_console.py` — terminal output used by `runtests`
- `ruff.toml`
- `mypy.ini`
- `pytest.ini`
- `.coveragerc`

Optional (copy only if you use the feature):

- `pyrightconfig.json` — only if `enable_basedpyright = true`
- `setup.cfg` — only if `enable_mutation_tests = true`. Keep its `[mutmut] source_paths` in sync with `source_paths` in `quality.toml`.
- `.pre-commit-config.yaml` — only if you use pre-commit
- `.github/workflows/ci.yml` — only if you use GitHub Actions
- `.vscode/settings.json` — only if you use VS Code
- `.gitignore`, `.python-version` — copy as needed

## Running Checks

```bash
./runtests                # tests, mypy, ruff lint, ruff format, in that order
./runtests --tests
./runtests --types
./runtests --lint
./runtests --format
./runtests --pyright      # optional, requires enable_basedpyright = true
./runtests --mutations    # optional, requires enable_mutation_tests = true
./runtests --tests -k some_test_name
```

## Coverage And Test Quality

100% coverage is required by default, but coverage alone does not prove tests are meaningful:

- line coverage proves code executed
- branch coverage proves decision paths executed
- mutation testing proves your tests actually detect behavior changes

Adjust `coverage_threshold` in `quality.toml` if your team needs a different bar.
