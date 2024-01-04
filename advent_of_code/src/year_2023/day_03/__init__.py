from advent_of_code.src.utils import BaseSolution
import re

NUM_REGEX = re.compile(r"\d+")
SYMBOLS = "$%/+=-&#@*"
GEAR = "*"


class Solution(BaseSolution):
    """Logics for solving day 3."""
    day = 3

    # example = True

    def part_1(self):
        """Return the sum of all the part numbers in the engine schematic."""
        total = 0
        symbol_regex = re.compile(r".*([$%/+=\-&#@*]).*")
        input_len = len(self.input_lines) - 1
        line_len = len(self.input_lines[0]) - 1
        for y, line in enumerate(self.input_lines):
            low_y = max(0, y - 1)
            high_y = min(input_len, y + 1)
            for match in NUM_REGEX.finditer(line):
                number = match.group()
                low_x = max(0, match.start() - 1)
                high_x = min(line_len, match.start() + len(number) + 1)
                for try_y in range(low_y, high_y + 1):
                    if symbol_regex.match(self.input_lines[try_y][low_x:high_x]):
                        total += int(number)
                        break
        return total

    def part_2(self):
        """Return the sum of all the gear ratios in your engine schematic."""
        total = 0
        symbol_regex = re.compile(r"\*")
        input_len = len(self.input_lines) - 1
        line_len = len(self.input_lines[0]) - 1
        gears = dict()
        for y, line in enumerate(self.input_lines):
            low_y = max(0, y - 1)
            high_y = min(input_len, y + 1)
            for match in NUM_REGEX.finditer(line):
                number = match.group()
                low_x = max(0, match.start() - 1)
                high_x = min(line_len, match.start() + len(number) + 1)
                for try_y in range(low_y, high_y + 1):
                    for match in symbol_regex.finditer(self.input_lines[try_y][low_x:high_x]):
                        # possible gear
                        key = (match.start()+low_x, try_y)
                        if key in gears:
                            gears[key].append(int(number))
                        else:
                            gears[key] = [int(number)]
        for num_list in gears.values():
            if len(num_list) != 2:
                continue
            total += num_list[0] * num_list[1]
        return total


