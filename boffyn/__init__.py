import sys

__version__ = "0.0.1"


def main():

    if sys.platform == "win32":
        print("boffyn does not support Windows.", file=sys.stderr)
        sys.exit(1)

    print("boffyn: Coming soon")
