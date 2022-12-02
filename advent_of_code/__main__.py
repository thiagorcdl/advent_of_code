#!/usr/bin/env python
"""Run main logic by calling the appropriate modules."""
import importlib
import sys
import logging

logger = logging.getLogger()


def parse_input(input_args) -> tuple:
    """Evaluate input arguments and return parsed data."""
    if len(input_args) < 3:
        sys.exit("Missing parameters!")

    year = int(input_args[1])
    day = int(input_args[2])
    part = len(input_args) > 3 and int(input_args[3]) or 1
    return year, day, part


def run_day_resolution(year: int, day: int, part: int = 1) -> None:
    """Import and execute the the part of resolution for the specified day."""
    year_module_name = f"year_{year}"
    day_module_name = f"day_{day:02d}"
    module_path = f"advent_of_code.src.{year_module_name}.{day_module_name}"
    logger.debug(f"\n\tmodule_path: {module_path}")

    try:
        module = importlib.import_module(module_path)
    except ModuleNotFoundError:
        print(f"Day {day} for year {year} hasn't been implemented yet.")
        return

    input_path = f"advent_of_code/src/{year_module_name}/{day_module_name}/input.txt"
    logger.debug(f"\n\tinput_path: {input_path}")
    with open(input_path, "r") as file:
        input_lines = file.read().splitlines()

    solver = module.Solution(input_lines)
    result = solver.run(part)
    print(result)


if __name__ == "__main__":
    logger.debug(f"\n\tsys.argv: {sys.argv}")
    year, day, part = parse_input(sys.argv)
    logger.debug(f"\n\tyear, day, part: {year, day, part}")

    run_day_resolution(year, day, part)

