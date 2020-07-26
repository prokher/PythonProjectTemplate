# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Development setup

1. Install PyEnv to be able to work with many Python versions at once
   [PyEnv→Installation](https://github.com/pyenv/pyenv#installation).
2. Install Python versions needed:
   ```shell
   $ pyenv local | xargs -L1 pyenv install
   ```
3. Install Poetry to the system Python.
   ```shell
   # Check if you have Poetry properly installed.
   $ poetry self update
   # Install Poetry to the system. Make sure virtualenv is not active!
   $ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
   ```
   It is important to install Poetry into the system Python, NOT in your
   virtual environment. For details see Poetry docs: https://python-poetry.org/docs/#installation
4.  Create local virtualenv in `.venv`, install all project dependencies
   (from `pyproject.toml`), and upgrade pip:
   ```bash
   $ poetry install && poetry run pip install --upgrade pip
   ```
11. Run tests:
   ```bash
   $ pytest
   ```
12. Open project directory in the VS Code and follow recommendations.