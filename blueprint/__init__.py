import toml

__version__ = toml.load("pyproject.toml")["tool"]["poetry"]["version"]

CONFIG = toml.load("config.toml")["app"]
