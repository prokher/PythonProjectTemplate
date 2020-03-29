# Python project template by Prokher

Python project template carefully baked by Prokher for personal use. If
you find it useful - you are welcome to use it as well.

This template is intended to automate Python project bootstrapping. At
the same time, you will not find scripts or commands for all possible
configuration management cases here. I think software engineer must
understand how tooling works and must be able to configure tools he
works with. So the target use-case is the following: you start with this
template, get working Python project, and then tune the results to
satisfy you project needs. To help with this I thoroughly commended all
the configuration files and left links to the relevant parts of the
documentation everywhere possible. Enjoy.

The template deploys by the awesome
[Cookiecutter](https://github.com/cookiecutter/cookiecutter) tool. If
one day you need to make a template for some project (e.g. a set for
structured folders and files) I recommend to take a look at the
Cookiecutter. The usage is indeed straightforward and it does its job
very well.

## Quick start

```bash
$ pip install cookiecutter
$ cookiecutter gh:prokher/PythonProjectTemplate
```

## Feedback

Please, do not bother me if you dislike some stylistic things. I've made
this template for personal use, after all. On the other hand, if you see
there is (objectively) better alternative to one of the tools used, or
something must be updated due to use latest version of these tools -
feel free to make an issue or PR. I would like to keep this template
up-to-date and kind of modern.

## Development setup

1. Install Poetry to the system Python.
   ```bash
   wget https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py
   python3.x get-poetry.py  # ← Replace 'x' with proper Python version.
   rm get-poetry.py
   ```
   It is important to install Poetry in the system Python. For details
   see Poetry docs: https://python-poetry.org/docs/#installation
2. Create local virtualenv in `.venv`, install all project dependencies
   (from `pyproject.toml`), and upgrade pip.:
   ```bash
   $ poetry install && poetry run pip install --upgrade pip
   ```

## License

This project is licensed under the terms of the [MIT License](/LICENSE).
