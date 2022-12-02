import re
import json

from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 12."""
    day = 12

    def solve(self, part2=False):
        injson = self.input_lines[0]

        def search(current):
            items = []
            if isinstance(current, dict):
                items = current.items()
            elif isinstance(current, list):
                items = enumerate(current)
            for key, item in items:
                if isinstance(item, dict):
                    current[key] = 0 if "red" in item.values() else search(item)
                elif isinstance(item, list):
                    current[key] = search(item)
            return current

        if part2:
            ldjson = json.loads(injson)
            ldjson = search(ldjson)
            injson = json.dumps(ldjson)

        return sum(map(int, re.findall(r'\-?\d+', injson)))

    def part_1(self):
        """Run solution for part 1."""
        return self.solve()

    def part_2(self):
        """Run solution for part 2."""
        return self.solve(part2=True)


