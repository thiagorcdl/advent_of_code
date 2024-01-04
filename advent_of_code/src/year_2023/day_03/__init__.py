from advent_of_code.src.utils import BaseSolution
import re

SYMBOLS = "$%/+=-&#@*"


class Solution(BaseSolution):
    """Logics for solving day 3."""
    day = 3

    # example = True

    def part_1(self):
        """Return the sum of all the part numbers in the engine schematic."""
        total = 0
        num_regex = re.compile(r"\d+")
        symbol_regex = re.compile(r".*([$%/+=\-&#@*]).*")
        input_len = len(self.input_lines) - 1
        line_len = len(self.input_lines[0]) - 1
        for y, line in enumerate(self.input_lines):
            low_y = max(0, y - 1)
            high_y = min(input_len, y + 1)
            for match in num_regex.finditer(line):
                number = match.group()
                low_x = max(0, match.start() - 1)
                high_x = min(line_len, match.start() + len(number) + 1)
                for try_y in range(low_y, high_y + 1):
                    if symbol_regex.match(self.input_lines[try_y][low_x:high_x]):
                        total += int(number)
                        break
        return total

    def part_2(self):
        """Run solution for part 2."""
        total = 0
        for line in self.input_lines:
            pass
        return total


