#!/usr/bin/env python
"""Run main logic by calling the appropriate modules."""
import importlib
import sys


def run_day_resolution(day: int, part: int = 1) -> None:
    """Import and execute the the part of resolution for the specified day."""
    module_name = f"day_{day:02d}"
    try:
        module = importlib.import_module(f"src.{module_name}")
    except ModuleNotFoundError:
        print(f"Day {day} hasn't been implemented yet.")
        return

    with open(f"./src/{module_name}/input.txt", "r") as file:
        input_lines = file.readlines()

    module.Resolution().run(part, input_lines)


if __name__ == "__main__":
    day = int(sys.argv[1])
    part = len(sys.argv) > 2 and int(sys.argv[2]) or 1
    # TODO: validate input
    run_day_resolution(day, part)

