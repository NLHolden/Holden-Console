import argparse
from collections.abc import Sequence
from pathlib import Path

from interface.application import run_console


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the Holden Console.")
    parser.add_argument(
        "config_file", type=Path, help="Path to the console JSON config"
    )
    args = parser.parse_args(argv)

    return run_console(args.config_file)


if __name__ == "__main__":
    raise SystemExit(main())
