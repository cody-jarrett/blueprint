import toml  # type: ignore

__version__ = toml.load("pyproject.toml")["tool"]["poetry"]["version"]
