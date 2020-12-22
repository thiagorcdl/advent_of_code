#!/usr/bin/env python
from src.utils import BaseResolution

TREE = "#"


class Resolution(BaseResolution):
    """Logics for resolving day 3."""
    day = 3

    @staticmethod
    def part_1(input_lines: list):
        """Run solution for part 1."""
        total = 0
        for i, line in enumerate(input_lines):
            idx = (i * 3) % len(line.strip())
            total += 1 if line[idx] == TREE else 0
        print(total)


