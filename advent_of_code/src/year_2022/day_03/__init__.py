from functools import reduce
from string import ascii_lowercase, ascii_uppercase

from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 3."""
    day = 3

    PRIORITIES = {
        char: i + 1
        for i, char in enumerate(ascii_lowercase + ascii_uppercase)
    }

    def part_1(self):
        """Find the item type that appears in both compartments of each rucksack.

        What is the sum of the priorities of those item types?
        """
        total = 0
        for line in self.input_lines:
            half = len(line) // 2
            line_list = list(line)
            first_set = set(line_list[:half])
            second_set = set(line_list[half:])
            repeat = first_set & second_set

            for char in repeat:
                total += self.PRIORITIES[char]

        return total

    def part_2(self):
        """Find the item type that corresponds to the badges of each three-Elf group.

        What is the sum of the priorities of those item types?
        """
        total = 0
        idx = 0
        while idx < len(self.input_lines):
            sack_group = self.input_lines[idx:idx + 3]
            repeat = reduce(lambda x, y: set(list(x)) & set(list(y)), sack_group)

            for char in repeat:
                total += self.PRIORITIES[char]

            idx += 3

        return total
