import toml
from dotenv import load_dotenv

from .secret import print_secret

APP_CONFIG = toml.load("config.toml")["app"]

load_dotenv(".env")


def app():
    """This is the main entrypoint to your application"""
    print(f"This is {APP_CONFIG.get('APP_NAME')}")
    print_secret()
