#!/usr/bin/env python
from advent_of_code.src.utils import BaseResolution


class Resolution(BaseResolution):
    """Logics for resolving day 1."""
    day = 1

    def part_1(self):
        """Count how many measurements are larger than the previous measurement."""
        total = 0
        previous_val = int(self.input_lines[0])

        for line in self.input_lines[1:]:
            current_val = int(line)
            if current_val > previous_val:
                total += 1
            previous_val = current_val

        return total

    def part_2(self):
        """Count how many sums are larger than the previous sum (3-value windows)."""
        self.input_lines = [
            int(val) + int(self.input_lines[i+1]) + int(self.input_lines[i + 2])
            for i, val in enumerate(self.input_lines[:-2])
        ]
        return self.part_1()


