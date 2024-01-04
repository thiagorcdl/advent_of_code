from advent_of_code.src.utils import BaseSolution
import re

class Solution(BaseSolution):
    """Logics for solving day 2."""
    day = 2
    games = []

    # example = True
    # > 1916

    def part_1(self):
        """Determine which games would have been possible if the bag had been loaded with
        only 12 red cubes, 13 green cubes, and 14 blue cubes.
        What is the sum of the IDs of those games?
        """
        minimums = {
            "red": 12,
            "green": 13,
            "blue": 14,
        }
        res = {
            "red": re.compile(r"(\d+) red"),
            "green": re.compile(r"(\d+) green"),
            "blue": re.compile(r"(\d+) blue"),
        }
        total = 0
        for idx, line in enumerate(self.input_lines):
            for color in minimums:
                matches = res[color].findall(line)
                maximum = max([int(x) for x in matches])
                if maximum > minimums[color]:
                    break
            else:
                total += idx + 1

        return total

    def part_2(self):
        """Run solution for part 2."""
        total = 0
        for line in self.input_lines:
            pass
        return total


