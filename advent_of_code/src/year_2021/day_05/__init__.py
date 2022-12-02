#!/usr/bin/env python
from advent_of_code.src.utils import BaseResolution


class Resolution(BaseResolution):
    """Logics for resolving day 5."""
    day = 5

    def process_diagonals(self, points, repeated_points, x1, y1, x2, y2) -> tuple:
        """Consider diagonals for part 2."""
        offset_x = abs(x2 - x1)
        offset_y = abs(y2 - y1)
        if offset_x == offset_y:
            # diagonal placement
            step_y = 1 if y1 < y2 else -1
            step_x = 1 if x1 < x2 else -1
            for i in range(offset_x+1):
                x = x1 + i * step_x
                y = y1 + i * step_y
                coords = (x, y)
                key = str(coords)
                if key in points:
                    repeated_points.add(key)
                else:
                    points.add(key)
        return points, repeated_points

    def part_1(self, allow_diagonals=False):
        """Find out at how many points at least two lines overlap."""
        points = set()
        repeated_points = set()
        for line in self.input_lines:
            same_x, same_y = False, False
            coords1, coords2 = [x.strip() for x in line.split("->")]
            x1, y1 = [int(x) for x in coords1.split(",")]
            x2, y2 = [int(x) for x in coords2.split(",")]

            if x1 == x2:
                same_x = True
            elif y1 == y2:
                same_y = True
            else:
                # Only consider horizontal or vertical lines
                if allow_diagonals:
                    points, repeated_points = self.process_diagonals(
                        points, repeated_points, x1, y1, x2, y2
                    )
                continue

            if same_x:
                # Horizontal placement
                a, b = (y1, y2) if y1 < y2 else (y2, y1)
                for y in range(a, b+1):
                    coords = (x1, y)
                    key = str(coords)
                    if key in points:
                        repeated_points.add(key)
                    else:
                        points.add(key)
            else:
                # Vertical placement
                a, b = (x1, x2) if x1 < x2 else (x2, x1)

                for x in range(a, b+1):
                    coords = (x, y1)
                    key = str(coords)
                    if key in points:
                        repeated_points.add(key)
                    else:
                        points.add(key)
        return len(repeated_points)

    def part_2(self):
        """Find out at how many points at least two lines overlap, also considering
        diagonals.
        """
        return self.part_1(allow_diagonals=True)


