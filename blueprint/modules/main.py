import os

import toml  # type: ignore
from dotenv import load_dotenv
from modules import __version__

load_dotenv(".env")

CONFIG = toml.load("config.toml")["app"]


def run() -> None:
    print(f"This is {CONFIG.get('APP_NAME')} {__version__}")
    print(f"Here's a test secret: {os.environ.get('TEST')}")
