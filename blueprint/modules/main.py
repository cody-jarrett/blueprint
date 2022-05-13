import os

import toml
from dotenv import load_dotenv
from modules import __version__

load_dotenv(".env")

CONFIG = toml.load("config.toml")["app"]

def run():
    print(f"This is {CONFIG.get('APP_NAME')} {__version__}")
    print(f"Here's a test secret: {os.environ.get('TEST')}")
