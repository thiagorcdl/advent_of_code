import math
import re
from functools import lru_cache

from advent_of_code.src.utils import BaseSolution

OPERATIONS = {
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
    "/": lambda x, y: x / y,
    "-": lambda x, y: x - y,
    "=": lambda x, y: x == y,
}
ME = "humn"
ROOT = "root"


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
                    "operation": OPERATIONS[match.group(3)],
                }
        return int(self.call_monkey(ROOT))

    def repl_expr(self, expr: str):
        replaced = True
        while replaced:
            replaced = False
            for monkey in self.monkeys.values():
                regex = monkey["regex"]
                expr, n_replaced = regex.subn(monkey["sub"], expr)
                if n_replaced:
                    replaced = True
        return expr

    def part_2(self):
        """Yield equation to be simplified.

        Used https://www.mathpapa.com/simplify-calculator/
        Got x = 889638042320048128/265335
        Got x = 3352886133830.999
        Rounded up to 3352886133831
        """
        for line in self.input_lines:
            if match := re.match(r"root: (\w+) ([*+/-]) (\w+)", line):
                monkey_name = ROOT
                self.monkeys[monkey_name] = {
                    "regex": re.compile(monkey_name),
                    "sub": f"({match.group(1)} == {match.group(3)})",
                }
            elif re.match(r"humn: (.+)", line):
                monkey_name = ME
                self.monkeys[monkey_name] = {
                    "regex": re.compile(monkey_name),
                    "sub": f"x",
                }
            elif match := re.match(r"(\w+): (\d+)", line):
                monkey_name = match.group(1)
                self.monkeys[monkey_name] = {
                    "regex": re.compile(monkey_name),
                    "sub": match.group(2),
                }
            elif match := re.match(r"(\w+): (.+)", line):
                monkey_name = match.group(1)
                self.monkeys[monkey_name] = {
                    "regex": re.compile(monkey_name),
                    "sub": f"({match.group(2)})",
                }
        expr = self.monkeys[ROOT]["sub"]
        return self.repl_expr(expr)
