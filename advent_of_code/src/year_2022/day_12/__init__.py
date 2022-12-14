from copy import copy
from string import ascii_lowercase
from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 12."""
    START_MARKER = "S"
    END_MARKER = "E"
    day = 12
    start_pos: tuple
    end_pos: tuple
    n_lines: int
    n_cols: int
    dir_map: list
    edges = []

    # example = True

    def parse_input(self):
        """Configure initial state."""

        self.n_lines = len(self.input_lines)
        self.n_cols = len(self.input_lines[0])
        self.dir_map = [
            [dict() for j in range(self.n_cols)]
            for i in range(self.n_lines)
        ]

        # Convert to numbers
        for l in range(self.n_lines):
            for c in range(self.n_cols):
                coords = l, c
                char = self.input_lines[l][c]

                if char == self.END_MARKER:
                    self.end_pos = coords
                    char = ascii_lowercase[-1]
                elif char == self.START_MARKER:
                    self.start_pos = coords
                    char = ascii_lowercase[0]

                self.dir_map[l][c]["val"] = ascii_lowercase.index(char)
                self.dir_map[l][c]["edges"] = []

        # Find edges
        for l in range(self.n_lines):
            for c in range(self.n_cols):
                val = self.dir_map[l][c]["val"]

                # Check up
                if l > 0 and self.dir_map[l - 1][c]["val"] <= val + 1:
                    self.edges.append((coords, (l - 1, c)))
                    self.dir_map[l][c]["edges"].append((l - 1, c))

                # Check left
                if c > 0 and self.dir_map[l][c - 1]["val"] <= val + 1:
                    self.edges.append((coords, (l, c - 1)))
                    self.dir_map[l][c]["edges"].append((l, c - 1))

                # Check down
                if l < self.n_lines-1 and self.dir_map[l + 1][c]["val"] <= val + 1:
                    self.edges.append((coords, (l + 1, c)))
                    self.dir_map[l][c]["edges"].append((l + 1, c))

                # Check right
                if c < self.n_cols-1 and self.dir_map[l][c + 1]["val"] <= val + 1:
                    self.edges.append((coords, (l, c + 1)))
                    self.dir_map[l][c]["edges"].append((l, c + 1))

    def bfs(self, pos:tuple, visited:set, steps=0):
        """Recursively traverse edges until reaches endpos."""
        lowest = float('inf')
        str_pos = str(pos)
        if str_pos in visited:
            return lowest
        if pos == self.end_pos:
            return steps

        visited.add(str_pos)
        l, c = pos
        for next_pos in self.dir_map[l][c]["edges"]:
            next_steps = self.bfs(next_pos, copy(visited), steps + 1)
            lowest = min(lowest, next_steps)

        return lowest

    def part_1(self):
        """Find the fewest steps required to move from start_pos to end_pos."""
        self.parse_input()
        return self.bfs(self.start_pos, set())

    def part_2(self):
        """Run solution for part 2."""
        total = 0
        for line in self.input_lines:
            pass
        return total
