#!/usr/bin/env python
from src.utils import BaseResolution


class Resolution(BaseResolution):
    """Logics for resolving day 5."""
    day = 5

    def get_seat_id(self, row, col):
        """Return seat ID."""
        return row * 8 + col

    def get_all_seat_ids(self, input_lines):
        """Yield all seat IDs."""
        for line in input_lines:
            row = 0
            for i, char in enumerate(line.strip()[6::-1]):
                row += (2 ** i) if char == "B" else 0
            col = 0
            for i, char in enumerate(line.strip()[-1:6:-1]):
                col += (2 ** i) if char == "R" else 0
            yield self.get_seat_id(row, col)

    def part_1(self, input_lines: list):
        """Find highest seat ID."""
        highest = max(self.get_all_seat_ids(input_lines))
        print(highest)

    def part_2(self, input_lines: list):
        """Find your seat ID (non-border gap)."""
        seat_ids = sorted(self.get_all_seat_ids(input_lines))
        for i in range(len(seat_ids) - 1):
            current = seat_ids[i]
            next_id = current + 1
            if seat_ids[i + 1] != next_id:
                print(next_id)
                break

