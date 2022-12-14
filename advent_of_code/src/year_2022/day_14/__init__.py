import re
import os
import time
from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 14."""
    day = 14
    cave = dict()
    simulated_cave: list
    n_lines = 0
    n_cols = 0
    floor = None
    SAND_ENTRY = 0, 500
    SAND = "."
    ROCK = "#"
    AIR = " "

    # example = True

    def print_cave(self):
        for line in self.simulated_cave:
            print(''.join(line))

    def build_cave(self):
        for line in self.input_lines:
            l1, c1 = None, None
            for vertex in re.findall(r"(\d+,\d+)", line):
                col, line = vertex.split(",")
                if l1 is None:
                    l1, c1 = int(line), int(col)
                    self.n_lines = max(self.n_lines, l1)
                    self.n_cols = max(self.n_cols, c1)
                    continue
                else:
                    l2, c2 = int(line), int(col)

                # Draw edge
                if l1 != l2:
                    # Vertical
                    for l in range(min(l1, l2), max(l1, l2) + 1):
                        try:
                            self.cave[c1].append(l)
                        except KeyError:
                            self.cave[c1] = [l]
                else:
                    # Horizontal
                    for c in range(min(c1, c2), max(c1, c2) + 1):
                        try:
                            self.cave[c].append(l1)
                        except KeyError:
                            self.cave[c] = [l1]
                self.n_lines = max(self.n_lines, l2)
                self.n_cols = max(self.n_cols, c2)
                l1, c1 = l2, c2

        for c in self.cave:
            self.cave[c].sort()

        self.simulated_cave = [
            [self.AIR for j in range(self.n_cols + 2)]
            for i in range(self.n_lines + 2)
        ]
        for c, lines in self.cave.items():
            for l in lines:
                self.simulated_cave[l][c] = self.ROCK

    def settle_sand(self, idx, line, col):
        """Add new sand obstacle."""
        self.cave[col].insert(idx, line)
        try:
            self.simulated_cave[line][col] = self.SAND
        except:
            pass
        return True

    def pour_sand(self, line=SAND_ENTRY[0], col=SAND_ENTRY[1]):
        """Simulate sand path."""
        if col not in self.cave:
            if self.floor is None:
                return None
            else:
                self.cave[col] = [self.floor]

        for i in range(len(self.cave[col])):
            stop_line = self.cave[col][i]
            if stop_line == line:
                # Cannot settle here
                if line == self.SAND_ENTRY[0]:
                    return None
                return False

            if stop_line > line:
                # Obstacle is in the way
                left_down = self.pour_sand(stop_line, col - 1)
                if left_down in [None, True]:
                    return left_down

                right_down = self.pour_sand(stop_line, col + 1)
                if right_down in [None, True]:
                    return right_down

                # Cannot go lower in any side, add sand above
                return self.settle_sand(i, stop_line - 1, col)
        return None

    def part_1(self):
        """Find how many units of sand come to rest before sand starts flowing into
        the abyss below.
        """
        total = 0
        self.build_cave()
        while self.pour_sand() is not None:
            total += 1
            # os.system('clear')
            # self.print_cave()
            # time.sleep(0.1)
        return total

    def part_2(self):
        """Run solution for part 2."""
        total = 0
        self.build_cave()

        self.floor = 2 + self.n_lines
        for c in self.cave:
            self.cave[c].append(self.floor)
        while self.pour_sand() is not None:
            total += 1
            # os.system('clear')
            # self.print_cave()
            # time.sleep(0.01)
        return total
