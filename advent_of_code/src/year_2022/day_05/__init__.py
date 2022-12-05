import re
from advent_of_code.src.utils import BaseSolution
from collections import deque


class Solution(BaseSolution):
    """Logics for solving day 5."""
    N_STACKS = 9
    CMD_LINE_START = 10
    day = 5
    stacks = [deque() for i in range(N_STACKS)]

    def get_stack(self, index):
        """Return 0-base index of a stack based on index in the string."""
        return (index - 1) // 4

    def build_stacks(self):
        """Read the first lines that tell the initial crate arrangement."""
        for line in self.input_lines[:self.CMD_LINE_START - 1]:
            for match in re.finditer(r'[A-Z]', line):
                stack_id = self.get_stack(match.start())
                crate = match.group()
                self.stacks[stack_id].appendleft(crate)

    def get_result(self):
        """Cocnatenate the top crates."""
        result = ""
        for stack in self.stacks:
            result += stack.pop()
        return result

    def part_1(self):
        """Find what crate ends up on top of each stack considering crates can only
        be lifted one by one.
        """
        self.build_stacks()

        for line in self.input_lines[self.CMD_LINE_START:]:
            amount, source, target = re.findall(r'(\d+) from (\d) to (\d)', line)[0]
            amount, source, target = int(amount), int(source) - 1, int(target) - 1
            while amount:
                amount -= 1
                crate = self.stacks[source].pop()
                self.stacks[target].append(crate)

        return self.get_result()

    def part_2(self):
        """Find what crate ends up on top of each stack considering multipel crates
        can be lifted at once.
        """
        self.build_stacks()

        for line in self.input_lines[self.CMD_LINE_START:]:
            amount, source, target = re.findall(r'(\d+) from (\d) to (\d)', line)[0]
            amount, source, target = int(amount), int(source) - 1, int(target) - 1
            fork = deque()
            while amount:
                amount -= 1
                crate = self.stacks[source].pop()
                fork.appendleft(crate)

            for crate in fork:
                self.stacks[target].append(crate)

        return self.get_result()
