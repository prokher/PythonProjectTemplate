"""Tests bootstrap sequence on the deployed template."""

import contextlib
import os
import pathlib
import subprocess


def test_bootstrap(cookies):
    """Test main bootsrap sequence: `poetry install` + `pytest`."""

    # Deploy template using default.
    bake_result = cookies.bake(template=str(pathlib.Path(__file__).parent.parent),)
    assert bake_result.exit_code == 0, "Baking failed!"
    assert bake_result.exception is None, "Baking failed!"

    # Prepare environment without virtualenv, cause we want Poetry to
    # create a new clean one inside the generated project.
    env = os.environ.copy()
    env.pop("VIRTUAL_ENV", None)

    with cd(str(bake_result.project)):
        subprocess.check_call(["poetry", "install"], env=env)
        subprocess.check_call(
            ["poetry", "run", "pip", "install", "--upgrade", "pip"], env=env
        )
        subprocess.check_call(["poetry", "run", "pytest"], env=env)


@contextlib.contextmanager
def cd(dirpath):
    """Context manager to temporary change working directory."""
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)
