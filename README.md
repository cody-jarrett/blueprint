# Basic Blueprint

Basic Python project structure taken from [Thuwarakesh Murallie](https://github.com/thuwarakeshm): [blueprint](https://github.com/thuwarakeshm/blueprint)

## Installation

Blueprint uses Poetry for dependency management: [Poetry official installation docs](https://python-poetry.org/docs/#installation)

After setting up a new project directory based on this one:

1. Install depenencies

```bash
poetry install
```

2. Install pre-commit hooks

```bash
poetry run pre-commit install
```

You're ready to go

## Usage

Now you can program your application inside the blueprint directory. The following command will start your application.

```bash
poetry run start
```

The above command will run the `app` function in the `main.py` module. You can import your custom functions and hook it to the `app` function to run them.

If not you can change the entry point to a different function by changing the `blueprint.main:app` configuration in the `pyproject.toml` file.

**To change the main module name**, you can rename the `blueprint` directory. But make sure you also rename the `name` in the `pyproject.toml` file.

**You can add project configuration** directly to the config toml file's `[app]` section. You can read it in anywhere in your project by calling the following lines:

```python
import toml
APP_CONFIG = toml.load("config.toml")["app"]

app_name = APP_CONFIG['APP_NAME']
```

You can also add app secrets directly to the `.env` file and read it anywhere from your project with the help of Python's built in `os` module.

```python
import os
secret = os.environ['APP_SECRET']
```

This is possible because we've loaded the env file from our `main.py` module. If you are replacing this module, be sure to load it again.

