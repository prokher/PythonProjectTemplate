"""Check code by running linters and style checkers."""

import pathlib

import plumbum
import pytest

SOURCE_DIRS = ["{{cookiecutter.root_python_package}}/", "tests/"]
PROJECT_ROOT_DIR = pathlib.Path(__file__).absolute().parent.parent


@pytest.mark.parametrize("src_dir", SOURCE_DIRS)
def test_pylint(src_dir):
    """Run Pylint."""

    pylint = plumbum.local["pylint"]
    with plumbum.local.cwd(PROJECT_ROOT_DIR):
        result = pylint(src_dir)
        if result:
            print("\nPylint:", result)


@pytest.mark.parametrize("src_dir", SOURCE_DIRS)
def test_black(src_dir):
    """Run Black."""
    black = plumbum.local["black"]
    with plumbum.local.cwd(PROJECT_ROOT_DIR):
        result = black("--check", src_dir)
        if result:
            print("\nBlack:", result)


@pytest.mark.parametrize("src_dir", SOURCE_DIRS)
def test_isort(src_dir):
    """Run Isort."""
    isort = plumbum.local["isort"]
    with plumbum.local.cwd(PROJECT_ROOT_DIR):
        result = isort("--check-only", "-rc", src_dir)
        if result:
            print("\nIsort:", result)


@pytest.mark.parametrize("src_dir", SOURCE_DIRS)
def test_mypy(src_dir):
    """Run MyPy."""
    mypy = plumbum.local["mypy"]
    with plumbum.local.cwd(PROJECT_ROOT_DIR):
        result = mypy(src_dir)
        if result:
            print("\nMyPy:", result)


@pytest.mark.parametrize("src_dir", SOURCE_DIRS)
def test_pydocstyle(src_dir):
    """Run Pydocstyle."""

    pydocstyle = plumbum.local["pydocstyle"]
    with plumbum.local.cwd(PROJECT_ROOT_DIR):
        result = pydocstyle(src_dir)
        if result:
            print("\nPydocstyle:", result)
