#!/usr/bin/env python
import re

from src.utils import BaseResolution


class Resolution(BaseResolution):
    """Logics for resolving day 2.

    Input format:
        min-max char: password
    """
    day = 2

    @staticmethod
    def part_1(input_lines: list):
        """Run solution for part 1."""
        valid = 0
        for line in input_lines:
            match = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
            char_min = int(match.group(1))
            char_max = int(match.group(2))
            char = match.group(3)
            password = match.group(4)
            if char_min <= password.count(char) <= char_max:
                valid += 1
        print(valid)

