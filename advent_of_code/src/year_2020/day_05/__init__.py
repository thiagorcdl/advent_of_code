#!/usr/bin/env python
from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 5."""
    day = 5

    def get_seat_id(self, row, col):
        """Return seat ID."""
        return row * 8 + col

    def get_all_seat_ids(self):
        """Yield all seat IDs."""
        for line in self.input_lines:
            row = 0
            for i, char in enumerate(line.strip()[6::-1]):
                row += (2 ** i) if char == "B" else 0
            col = 0
            for i, char in enumerate(line.strip()[-1:6:-1]):
                col += (2 ** i) if char == "R" else 0
            yield self.get_seat_id(row, col)

    def part_1(self):
        """Find highest seat ID."""
        highest = max(self.get_all_seat_ids())
        return highest

    def part_2(self):
        """Find your seat ID (non-border gap)."""
        seat_ids = sorted(self.get_all_seat_ids())
        for i in range(len(seat_ids) - 1):
            current = seat_ids[i]
            next_id = current + 1
            if seat_ids[i + 1] != next_id:
                return next_id

