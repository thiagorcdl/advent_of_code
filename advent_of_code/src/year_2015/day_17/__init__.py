import re

from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 17."""
    day = 17

    def solve(self, part2=False):
        eggnog = 150
        refr = list(map(int, re.findall(r'(\d+)', self.raw_input)))
        size = len(refr)
        answers = []

        def search(last_sum, start, answer):
            for i in range(start, size):
                cur_sum = last_sum + refr[i]
                cur_answer = answer + [refr[i], ]
                if cur_sum < eggnog:
                    search(cur_sum, i + 1, cur_answer)
                elif cur_sum == eggnog:
                    answers.append(cur_answer)

        search(0, 0, [])
        lengths = list(map(len, answers))
        return lengths.count(min(lengths)) if part2 else len(answers)

    def part_1(self):
        """Run solution for part 1."""
        return self.solve()

    def part_2(self):
        """Run solution for part 2."""
        return self.solve(part2=True)
