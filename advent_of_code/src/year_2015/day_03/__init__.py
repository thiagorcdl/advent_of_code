#!/usr/bin/env python
from advent_of_code.src.utils import BaseResolution


class Resolution(BaseResolution):
    """Logics for resolving day 3."""
    day = 3

    def solve(self, part=1):
        """Run core logics for resolving day 1."""
        directions = {
            '^': (0, 1),
            '>': (1, 0),
            'v': (0, -1),
            '<': (-1, 0)
        }
        turn = 0
        visited = [(0, 0), ]
        current = [(0, 0), (0, 0)]

        for char in self.input_lines[0]:
            current[turn] = tuple(map(sum, zip(current[turn], directions[char])))
            visited.append(current[turn])
            if part == 2:
                turn ^= 1
        return len(set(visited))

    def part_1(self):
        """Run solution for part 1."""
        return self.solve()

    def part_2(self):
        """Run solution for part 2."""
        return self.solve(part=2)
