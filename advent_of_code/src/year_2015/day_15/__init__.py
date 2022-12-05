import re

from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 15."""
    day = 15

    def solve(self, part2=False):
        pattern = (
            r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), '
            r'texture (-?\d+), calories (-?\d+)'
        )
        ingr = []
        [ingr.append(list(map(int, [cap, dur, flav, tex, cal]))) for
         name, cap, dur, flav, tex, cal in re.findall(pattern, self.raw_input)]
        recipe = [0, 0, 0, 0]

        best = 0
        for i in reversed(range(101)):
            recipe[0] = i
            for j in range(100 - i):
                recipe[1] = j
                for k in range(100 - i - j):
                    recipe[2] = k
                    recipe[3] = 100 - i - j - k
                    if part2 and sum(
                        [ingr[x][4] * recipe[x] for x in range(4)]) != 500:
                        continue
                    cap = max(sum([ingr[x][0] * recipe[x] for x in range(4)]), 0)
                    dur = max(sum([ingr[x][1] * recipe[x] for x in range(4)]), 0)
                    flav = max(sum([ingr[x][2] * recipe[x] for x in range(4)]), 0)
                    tex = max(sum([ingr[x][3] * recipe[x] for x in range(4)]), 0)
                    best = max(best, cap * dur * flav * tex)
        return best

    def part_1(self):
        """Run solution for part 1."""
        return self.solve()

    def part_2(self):
        """Run solution for part 2."""
        return self.solve(part2=True)
