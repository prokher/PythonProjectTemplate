"""Entrypoint of the `{{cookiecutter.root_python_package}}` package.

Run by `python -m {{cookiecutter.root_python_package}}`.
"""

import sys

import invoke

# Docs:
# - Invoke: Pythonic task execution.
#   http://docs.pyinvoke.org/en/latest/


@invoke.task
def hello_world(ctx):
    """Hello world task."""
    # Remove unused variable.
    del ctx

    print("Hello world!")


# ------------------------------------------------------------------------- INVOKE SETUP

ROOT = invoke.Collection()
ROOT.add_task(hello_world)

if __name__ == "__main__":

    class Config(invoke.config.Config):
        """Custom Invoke configuration."""

        @staticmethod
        def global_defaults():
            """Overwrite default Invoke configuration."""
            defaults = invoke.config.Config.global_defaults()
            # Tune the Invoke configuration:
            #     pty: Use PTY to get colored output.
            #     warn: Stop execution when a command fails (use '-w' to
            #         change this behavior).
            #     echo: Output executed commands.
            #     autoprint: Automatically print this task’s return
            #         value to standard output when invoked directly
            #         via the CLI.
            # NOTE: Params can be overwritten outside by the environment
            # variables: 'INVOKE_RUN_WARN', 'INVOKE_RUN_PTY', ...
            overrides = {
                "run": {"pty": True, "warn": False, "echo": True, "autoprint": True}
            }
            return invoke.config.merge_dicts(defaults, overrides)

    def main():
        """Package `{{cookiecutter.root_python_package}}` entrypoint.

        This main entrypoint function executes when you run
        `python -m {{cookiecutter.root_python_package}}`.

        """
        program = invoke.Program(
            namespace=ROOT, name="{{cookiecutter.project_name}}", config_class=Config
        )
        program.run()

    sys.exit(main())
