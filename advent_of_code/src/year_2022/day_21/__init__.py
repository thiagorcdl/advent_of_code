import math
import re
from functools import lru_cache

from advent_of_code.src.utils import BaseSolution

OPERATIONS = {
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
    "/": lambda x, y: x / y,
    "-": lambda x, y: x - y,
}


class Solution(BaseSolution):
    """Logics for solving day 21."""
    day = 21
    monkeys = dict()

    # example = True

    def call_monkey(self, monkey_name: str):
        monkey = self.monkeys[monkey_name]
        if monkey["val"] is not None:
            return monkey["val"]
        result0 = self.call_monkey(monkey["operands"][0])
        result1 = self.call_monkey(monkey["operands"][1])
        return monkey["operation"](result0, result1)

    def part_1(self):
        """Run solution for part 1."""
        for line in self.input_lines:
            if match := re.match(r"(\w+): (\d+)", line):
                self.monkeys[match.group(1)] = {"val": int(match.group(2))}
            elif match := re.match(r"(\w+): (\w+) ([*+/-]) (\w+)", line):
                self.monkeys[match.group(1)] = {
                    "val": None,
                    "operands": [match.group(2), match.group(4)],
                    "operator": match.group(3),
                    "operation": OPERATIONS[match.group(3)],
                }
        return int(self.call_monkey("root"))

    def part_2(self):
        """Run solution for part 2."""
        total = 0
        for line in self.input_lines:
            pass
        return total
