import re

from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 8."""
    day = 8

    def part_1(self):
        """Run solution for part 1."""
        n_code = 0
        n_encoded = 0
        n_decoded = 0
        for line in self.input_lines:
            n_code += len(line)
            decoded = re.sub(r'\\x[0-9A-Fa-f][0-9A-Fa-f]|\\"|\\\\', '-', line)[1:-1]
            n_decoded += len(decoded)
        return n_code - n_decoded

    def part_2(self):
        """Run solution for part 2."""
        n_code = 0
        n_encoded = 0
        n_decoded = 0
        for line in self.input_lines:
            n_code += len(line)
            encoded = '"' + line.replace('\\', '\\\\').replace(r'"', r'\"') + '"'
            n_encoded += len(encoded)

        return n_encoded - n_code
