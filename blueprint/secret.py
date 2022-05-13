import os


def print_secret():
    print(f"Here's a test secret: {os.environ.get('TEST')}")
