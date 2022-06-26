import os

import toml  # type: ignore
from dotenv import load_dotenv

from blueprint import __version__

load_dotenv(".env")

CONFIG = toml.load("config.toml")["app"]


def start() -> None:
    print(f"This is {CONFIG.get('NAME')} {__version__}")
    print(f"Here's a test secret: {os.environ.get('TEST')}")
