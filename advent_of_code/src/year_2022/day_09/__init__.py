from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 9."""
    day = 9
    example = True
    visited = set()

    def visit(self, position: tuple):
        """Add position to set."""
        self.visited.add(f"{position[0]},{position[1]}")

    def part_1(self):
        """Run solution for part 1."""
        head = tail = starting_pos = 0, 0
        self.visit(tail)

        dir_map = {
            "U": lambda pos, n: (pos[0] - n, pos[1]),
            "R": lambda pos, n: (pos[0], pos[1] + n),
            "D": lambda pos, n: (pos[0] + n, pos[1]),
            "L": lambda pos, n: (pos[0], pos[1] - n),
        }
        follow_map = {
            "U": lambda pos: (pos[0] + 1, pos[1]),
            "R": lambda pos: (pos[0], pos[1] - 1),
            "D": lambda pos: (pos[0] - 1, pos[1]),
            "L": lambda pos: (pos[0], pos[1] + 1),
        }

        for line in self.input_lines:
            direction, amount = line.split()
            head = dir_map[direction](head, int(amount))
            if abs(head[0] - tail[0]) > 2 or abs(head[1] - tail[1]) > 2:
                tail = follow_map[direction](head)

        return len(self.visited)

    def part_2(self):
        """Run solution for part 2."""
        total = 0
        for line in self.input_lines:
            pass
        return total
