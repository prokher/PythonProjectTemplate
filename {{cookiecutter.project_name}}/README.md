# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Development setup

1. Make sure Poetry installed in the system Python. Install it if not.
   ```bash
   # Check if you have Poetry properly installed.
   $ poetry self update
   # Install Poetry to the system. Make sure virtualenv is not active!
   $ wget https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py
   $ python3.x get-poetry.py  # ← Replace 'x' with proper Python version.
   $ rm get-poetry.py
   ```
   It is important to install Poetry to the system Python. For details
   see Poetry docs: https://python-poetry.org/docs/#installation
2. Create local virtualenv in `.venv`, install all project dependencies
   (from `pyproject.toml`), and upgrade pip:
   ```bash
   $ poetry install --no-root && poetry run pip install --upgrade pip
   ```
3. Run tests:
   ```bash
   $ pytest
   ```
4. Open project directory in the VS Code and follow recommendations.
