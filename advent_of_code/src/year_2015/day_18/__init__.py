import itertools
import copy

from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 18."""
    day = 18

    def solve(self, part2=False):
        grid = []
        n_steps = 100
        size = 100
        corners = [(0, 0), (0, size - 1), (size - 1, 0), (size - 1, size - 1)]

        for line in self.input_lines:
            grid.append(list(map(lambda x: 0 if x == '.' else 1, list(line))))

        for i, j in corners:
            grid[i][j] = 1
        grid2 = copy.deepcopy(grid)
        for s in range(n_steps):
            for i in range(size):
                for j in range(size):
                    neighbors = list(itertools.chain(
                        *map(lambda x: x[max(j - 1, 0):min(j + 2, size)],
                             grid[max(i - 1, 0):min(i + 2, size)])))
                    n_on = sum(neighbors) - (1 if grid[i][j] else 0)
                    if (grid[i][j] and n_on not in [2, 3]) or (
                        not grid[i][j] and n_on == 3):
                        if part2 and grid[i][j] and (i, j) in corners:
                            continue
                        grid2[i][j] = grid[i][j] ^ 1
            grid = copy.deepcopy(grid2)
        return sum(map(sum, grid))

    def part_1(self):
        """Run solution for part 1."""
        return self.solve()

    def part_2(self):
        """Run solution for part 2."""
        return self.solve(part2=True)
