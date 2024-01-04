from advent_of_code.src.utils import BaseSolution
import re


class Solution(BaseSolution):
    """Logics for solving day 0."""
    day = 0

    def part_1(self):
        """Return the sum of all the calibration values."""
        total = 0
        regex = re.compile(r'(\d)')
        for line in self.input_lines:
            results = regex.findall(line)
            if not results:
                continue
            total += int(results[0] + results[-1])
        return total

    def part_2(self):
        """Run solution for part 2."""
        total = 0
        for line in self.input_lines:
            pass
        return total


