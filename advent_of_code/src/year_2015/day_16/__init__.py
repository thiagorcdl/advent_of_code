import re

from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 17."""
    day = 17

    def solve(self, part2=False):
        aunt = []
        truth = {
            'children': 3,
            'cats': 7,
            'samoyeds': 2,
            'pomeranians': 3,
            'akitas': 0,
            'vizslas': 0,
            'goldfish': 5,
            'trees': 3,
            'cars': 2,
            'perfumes': 1,
        }
        naunt = 1
        matches = 0
        aunt = 0

        for line in self.input_lines:
            clues = {}

            for x in re.split(r'\d+: ', line)[1].split(','):
                key, val = x.split(":")
                key = key.lstrip().rstrip()
                val = int(val)
                if part2 and ((key in ['cats', 'trees'] and val <= truth[key]) or
                              (key in ['pomeranians', 'goldfish'] and val >= truth[
                                  key]) or
                              (truth[key] != val)) or truth[key] != val:
                    continue
                clues[key] = val
            aunt, matches = (naunt, len(clues)) if len(clues) > matches else (
                aunt, matches)
            naunt += 1
        return aunt

    def part_1(self):
        """Run solution for part 1."""
        return self.solve()

    def part_2(self):
        """Run solution for part 2."""
        return self.solve(part2=True)
