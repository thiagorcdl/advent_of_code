#!/usr/bin/env python
import re

from advent_of_code.src.utils import BaseResolution


class Resolution(BaseResolution):
    """Logics for resolving day 2.

    Input format:
        min-max char: password
    """
    day = 2

    def part_1(self):
        """Run solution for part 1."""
        valid = 0
        for line in self.input_lines:
            match = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
            char_min = int(match.group(1))
            char_max = int(match.group(2))
            char = match.group(3)
            password = match.group(4)
            if char_min <= password.count(char) <= char_max:
                valid += 1
        return valid

    def part_2(self):
        """Run solution for part 2."""
        valid = 0
        for line in self.input_lines:
            match = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
            pos_1 = int(match.group(1)) - 1
            pos_2 = int(match.group(2)) - 1
            char = match.group(3)
            password = match.group(4)
            chars = {password[pos_1], password[pos_2]}
            if len(chars) > 1 and char in chars:
                valid += 1
        return valid

