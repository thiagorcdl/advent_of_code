from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 6."""
    day = 6

    grid = [[0 for x in range(1000)] for y in range(1000)]

    def part_1(self):
        """Run solution for part 1."""

        def turnon(i, j):
            self.grid[i][j] = 1

        def turnoff(i, j):
            self.grid[i][j] = 0

        def toggle(i, j):
            self.grid[i][j] = self.grid[i][j] ^ 1

        for line in self.input_lines:
            line = line.replace('turn ', 'turn')  # normalizes amount of arguments
            action, ia_ja, through, ib_jb = line.split(' ')
            ia, ja = map(lambda x: int(x), ia_ja.split(','))
            ib, jb = map(lambda x: int(x), ib_jb.split(','))
            for i in range(ia, ib + 1):
                for j in range(ja, jb + 1):
                    eval("%s(i,j)" % action)

        return sum(map(sum, self.grid))

    def part_2(self):
        """Run solution for part 2."""

        def turnon(i, j):
            self.grid[i][j] = self.grid[i][j] + 1

        def turnoff(i, j):
            self.grid[i][j] = max(self.grid[i][j] - 1, 0)

        def toggle(i, j):
            self.grid[i][j] = self.grid[i][j] + 2

        for line in self.input_lines:
            line = line.replace('turn ', 'turn')  # normalizes amount of arguments
            action, ia_ja, through, ib_jb = line.split(' ')
            ia, ja = map(lambda x: int(x), ia_ja.split(','))
            ib, jb = map(lambda x: int(x), ib_jb.split(','))
            for i in range(ia, ib + 1):
                for j in range(ja, jb + 1):
                    eval("%s(i,j)" % action)

        return sum(map(sum, self.grid))
