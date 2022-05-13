import os

import toml
from dotenv import load_dotenv

from blueprint import __version__

CONFIG = toml.load("config.toml")["app"]

load_dotenv(".env")


def app():
    print(f"This is {CONFIG.get('APP_NAME')} {__version__}")
    print(f"Here's a test secret: {os.environ.get('TEST')}")
