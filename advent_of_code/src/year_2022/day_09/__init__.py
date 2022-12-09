from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 9."""
    day = 9
    visited = set()
    INITIAL_POS = 0, 0
    N_KNOTS = 10
    DIR_MAP = {
        "U": lambda pos: (pos[0] - 1, pos[1]),
        "R": lambda pos: (pos[0], pos[1] + 1),
        "D": lambda pos: (pos[0] + 1, pos[1]),
        "L": lambda pos: (pos[0], pos[1] - 1),
    }

    def visit(self, position: tuple):
        """Add position to set."""
        self.visited.add(f"{position[0]},{position[1]}")

    def part_1(self):
        """Find how many positions does the tail of the rope visit when there is only
        a head knot and a tail.
        """
        head = tail = self.INITIAL_POS
        self.visit(tail)

        follow_map = {
            "U": lambda pos: (pos[0] + 1, pos[1]),
            "R": lambda pos: (pos[0], pos[1] - 1),
            "D": lambda pos: (pos[0] - 1, pos[1]),
            "L": lambda pos: (pos[0], pos[1] + 1),
        }

        for line in self.input_lines:
            direction, amount = line.split()
            for i in range(int(amount)):
                head = self.DIR_MAP[direction](head)
                if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                    tail = follow_map[direction](head)
                    self.visit(tail)

        return len(self.visited)

    def get_displacement(self, head: tuple, tail: tuple) -> list:
        """Return amount to add to tail's position based on head's position."""
        displacement = [0, 0]
        for i in range(2):
            if head[i] > tail[i]:
                displacement[i] = 1
            elif head[i] < tail[i]:
                displacement[i] = -1
        return displacement

    def follow(self, head: tuple, tail: tuple) -> tuple:
        """Return new tail position."""
        displacement = self.get_displacement(head, tail)
        return tail[0] + displacement[0], tail[1] + displacement[1]

    def part_2(self):
        """Find how many positions does the tail of the rope visit when there are
        ten knots in total.
        """
        knots = [self.INITIAL_POS for _ in range(self.N_KNOTS)]
        self.visit(knots[-1])

        for line in self.input_lines:
            direction, amount = line.split()
            for i in range(int(amount)):
                knots[0] = self.DIR_MAP[direction](knots[0])
                # Propagate movement through knots
                for j in range(1, self.N_KNOTS):
                    knot = knots[j]
                    prev = knots[j - 1]
                    if abs(prev[0] - knot[0]) > 1 or abs(prev[1] - knot[1]) > 1:
                        knots[j] = self.follow(prev, knot)
                self.visit(knots[-1])

        return len(self.visited)
