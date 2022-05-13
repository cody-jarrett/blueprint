import toml

__version__ = toml.load("pyproject.toml")["tool"]["poetry"]["version"]

# Add ROOT_DIR variable, containing the absolute path to the location of the package?
# Add the configuration of the logger for the package?
