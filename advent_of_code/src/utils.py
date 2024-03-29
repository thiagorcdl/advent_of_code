import sys

from advent_of_code.src.constants import HIGH_RECURSION_LIMIT


class BaseSolution:
    """Base class to be used by each day."""
    day = 0
    raw_input: str = ""
    input_lines: list = []
    limit_recursion = True
    example = False

    def __init__(self, raw_input: str):
        super().__init__()
        self.raw_input = raw_input
        self.input_lines = raw_input.splitlines()

        if not self.limit_recursion:
            sys.setrecursionlimit(HIGH_RECURSION_LIMIT)

    def part_1(self):
        """Run solution for part 1."""
        raise NotImplementedError

    def part_2(self):
        """Run solution for part 2."""
        raise NotImplementedError

    def run(self, part: int):
        """Execute the method corresponding to the specified part."""
        method_map = {
            1: self.part_1,
            2: self.part_2,
        }
        method = method_map[part]
        return method()
