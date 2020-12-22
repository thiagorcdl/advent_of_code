#!/usr/bin/env python
import sys
sys.path.append("..")
from src.utils import BaseResolution


class Resolution(BaseResolution):
    """Logics for resolving day 1."""
    day = 1

    @staticmethod
    def part_1(input_lines: list):
        """Run n**2 solution for part 1."""
        total = 2020
        for i, line in enumerate(input_lines):
            line = int(line)
            rest = total - line
            for candidate in input_lines[i+1:]:
                candidate = int(candidate)
                if rest == candidate:
                    print(line * candidate)
