"""Tests that template deploys successfully."""

import pathlib
from typing import Set


def test_project_directories(cookies):
    """Test resulting project has all expected files and directories."""

    expected_files = {
        ".gitignore",
        ".python-version",
        ".vscode",
        ".vscode/extensions.json",
        ".vscode/settings.json",
        "poetry.toml",
        "pyproject.toml",
        "README.md",
        "setup.cfg",
        "test_stuff",
        "test_stuff/__init__.py",
        "test_stuff/__main__.py",
        "tests",
        "tests/__init__.py",
        "tests/test_linters.py",
    }

    prj_params = {
        "project_name": "TestStuff",
        "project_description": "TestStuff description.",
        "version": "0.42.0",
        "license": "MIT",
        "root_python_package": "test_stuff",
        "full_name": "Tester",
        "email": "tester@example.com",
        "github_username": "tester",
        "pypi_project_name": "test-stuff",
        "pypi_repository": "https://github.com/tester/test-stuff",
        "pypi_homepage": "https://github.com/tester/test-stuff",
    }

    bake_result = cookies.bake(
        template=str(pathlib.Path(__file__).parent.parent), extra_context=prj_params,
    )
    assert bake_result.exit_code == 0, "Baking failed!"
    assert bake_result.exception is None, "Baking failed!"

    prj_path = pathlib.Path(bake_result.project)
    assert (
        prj_path.stem == prj_params["project_name"]
    ), "Resulting project directory name is wrong!"
    assert prj_path.is_dir(), "Resulting project directory does not exist!"

    # List all files and directories to compare with the expected set.
    all_files: Set[str] = set()
    fs_items = list(prj_path.iterdir())
    for fs_item in fs_items:
        all_files.add(str(fs_item.relative_to(prj_path)))
        if fs_item.is_dir():
            fs_items.extend(list(fs_item.iterdir()))

    assert (
        all_files == expected_files
    ), "Resulting project file structure differs from the expected one!"

    assert (
        prj_path / prj_params["root_python_package"]
    ).is_dir(), "Resulting project does not contain proper packager directory!"
