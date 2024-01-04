from advent_of_code.src.utils import BaseSolution
import re


DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

class Solution(BaseSolution):
    """Logics for solving day 1."""
    day = 1

    # example = True

    def part_1(self):
        """Return the sum of all the calibration values."""
        total = 0
        regex = re.compile(r"(\d)")
        for line in self.input_lines:
            results = regex.findall(line)
            if not results:
                continue
            total += int(results[0] + results[-1])
        return total

    def part_2(self):
        """Return the sum of all the calibration values with spelled-out numbers."""
        total = 0
        regex = re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))")
        for line in self.input_lines:
            results = regex.findall(line)
            if not results:
                continue
            total += int(DIGITS[results[0]] + DIGITS[results[-1]])
        return total


