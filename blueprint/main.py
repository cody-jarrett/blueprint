import os

from dotenv import load_dotenv

from blueprint import __version__

load_dotenv(".env")


def start() -> None:
    print(f"{__version__}")
    print(f"Here's a test secret: {os.environ.get('TEST')}")
