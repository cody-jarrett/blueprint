import os

import toml
from dotenv import load_dotenv

CONFIG = toml.load("config.toml")["app"]

load_dotenv(".env")


def app():
    """This is the main entrypoint to your application"""
    print(f"This is {CONFIG.get('APP_NAME')}")
    print(f"Here's a test secret: {os.environ.get('TEST')}")
