from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 8."""
    day = 8
    n_lines = 0
    n_columns = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.n_lines = len(self.input_lines)
        self.n_columns = len(self.input_lines[0])

    def part_1(self):
        """Find how many trees are visible from outside the grid."""
        visible = set()

        # Left to right
        for i in range(self.n_lines):
            prev = -1
            for j in range(self.n_columns):
                tree = int(self.input_lines[i][j])
                if tree > prev:
                    visible.add(f"{i},{j}")
                    prev = tree

        # Up to down
        for j in range(self.n_columns):
            prev = -1
            for i in range(self.n_lines):
                tree = int(self.input_lines[i][j])
                if tree > prev:
                    visible.add(f"{i},{j}")
                    prev = tree

        # Right to left
        for i in range(self.n_lines):
            prev = -1
            for j in range(self.n_columns - 1, 0, -1):
                tree = int(self.input_lines[i][j])
                if tree > prev:
                    visible.add(f"{i},{j}")
                    prev = tree

        # Down to up
        for j in range(self.n_columns):
            prev = -1
            for i in range(self.n_lines - 1, 0, -1):
                tree = int(self.input_lines[i][j])
                if tree > prev:
                    visible.add(f"{i},{j}")
                    prev = tree
        return len(visible)

    def get_scenic_score(self, line: int, col: int) -> int:
        """Traverse all directions until view is blocked."""
        scenic_score = 1
        tree = self.input_lines[line][col]

        # Right
        i = col + 1
        count = 0
        while i < self.n_columns:
            count += 1
            if self.input_lines[line][i] >= tree:
                break
            i += 1
        scenic_score *= count

        # Left
        count = 0
        i = col - 1
        while i >= 0:
            count += 1
            if self.input_lines[line][i] >= tree:
                break
            i -= 1
        scenic_score *= count

        # Down
        count = 0
        i = line + 1
        while i < self.n_lines:
            count += 1
            if self.input_lines[i][col] >= tree:
                break
            i += 1
        scenic_score *= count

        # Up
        count = 0
        i = line - 1
        while i >= 0:
            count += 1
            if self.input_lines[i][col] >= tree:
                break
            i -= 1
        scenic_score *= count

        return scenic_score

    def part_2(self):
        """Find the highest scenic score possible for any tree."""
        highest_score = 0

        for i in range(1, self.n_lines-1):
            for j in range(1, self.n_columns-1):
                score = self.get_scenic_score(i, j)
                highest_score = max(highest_score, score)
        return highest_score
