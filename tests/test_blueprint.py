import toml

name = toml.load("pyproject.toml")["tool"]["poetry"]["name"]


def test_name() -> None:
    assert name == "blueprint"
