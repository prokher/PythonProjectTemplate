# Python project template by Prokher

A Python project template is carefully baked by Prokher for personal
use. If you find it useful - you are welcome to use it as well.

This template is intended to automate Python project bootstrapping. At
the same time, you will not find scripts or commands for all possible
configuration management cases here. I think software engineers must
understand how tooling works and must be able to configure tools he
works with. So the target use-case is the following: you start with this
template, get a working Python project, and then tune the results to
satisfy your project needs. To help with this I thoroughly commended all
the configuration files and left links to the relevant parts of the
documentation everywhere possible. Enjoy.

The template deploys by the awesome
[Cookiecutter](https://github.com/cookiecutter/cookiecutter) tool. If
one day you need to make a template for some project (e.g. a set for
structured folders and files) I recommend to take a look at the
Cookiecutter. The usage is indeed straightforward and it does its job
very well.

## Features

- [Poetry](https://python-poetry.org) package and dependency manager.
- [Pytest](https://pytest.org) testing framework.
- [Black](https://black.readthedocs.io/en/stable/) code formatter.
- [isort](https://github.com/timothycrosley/isort) import formatter.
- [MyPy](http://mypy-lang.org) type checker.
- [Pylint](https://www.pylint.org) code checker.
- [Pydocstyle](http://www.pydocstyle.org/) docstrings checher.
- [Visual Studio Code](https://code.visualstudio.com).
- Test
  [test_linters.py]({{cookiecutter.project_name}}/tests/test_linters.py)
  runs linters (MyPy, Pylint) and check code style (Black, Isort,
  Pydocstyle).

## Quick start

```bash
$ pip install cookiecutter
$ cookiecutter gh:prokher/PythonProjectTemplate
$ cd <NewProject>
$ poetry install
$ poetry run pytest
$ code .
```

![quickstart.gif](quickstart.gif)

Congratulations, you have working Python project. Read its `README.md`
to see how to setup your development environment properly. I also
recommend reading generated configuration files `pyproject.toml` and
`setup.cfg` to check if they match your needs.

## Feedback

Please, do not bother me if you dislike some stylistic things. I've made
this template for personal use, after all. On the other hand, if you see
there is (objectively) better alternative to one of the tools used, or
something must be updated due to use latest version of these tools -
feel free to make an issue or PR. I would like to keep this template
up-to-date and kind of modern.

## Development setup

1. Install PyEnv to be able to work with many Python versions at once
   [PyEnv→Installation](https://github.com/pyenv/pyenv#installation).
2. Install Python versions needed:
   ```shell
   $ pyenv local | xargs -L1 pyenv install
   ```
3. Install Poetry to the system Python.
   ```shell
   $ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
   ```
   It is important to install Poetry into the system Python, NOT in your
   virtual environment. For details see Poetry docs: https://python-poetry.org/docs/#installation
4. Create local virtualenv in `.venv`, install all project dependencies
   (from `pyproject.toml`), and upgrade pip.:
   ```bash
   $ poetry install && poetry run pip install --upgrade pip
   ```

## License

This project is licensed under the terms of the [MIT License](/LICENSE).
