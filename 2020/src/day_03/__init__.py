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

    @staticmethod
    def part_2(input_lines: list):
        """Run solution for part 2."""
        total = 1
        pairs = (
            (1, 1),
            (3, 1),
            (5, 1),
            (7, 1),
            (1, 2),
        )
        for right, down in pairs:
            partial = 0
            for i, j in enumerate(range(0, len(input_lines), down)):
                line = input_lines[j]
                idx = (i * right) % len(line.strip())
                partial += 1 if line[idx] == TREE else 0
            total *= partial
        print(total)

