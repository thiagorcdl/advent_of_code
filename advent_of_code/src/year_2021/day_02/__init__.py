#!/usr/bin/env python
from advent_of_code.src.utils import BaseResolution


class Resolution(BaseResolution):
    """Logics for resolving day 2."""
    day = 2

    def part_1(self):
        """Calculate the horizontal position and depth after following the planned
        course, and multiply them.
        """
        horizontal = 0
        depth = 0

        for line in self.input_lines:
            command, value = line.split()
            value = int(value)

            if command == "forward":
                horizontal += value
            elif command == "up":
                depth -= value
            elif command == "down":
                depth += value

        return horizontal * depth

    def part_2(self):
        """Calculate the horizontal position and depth after following the planned
        course using aim, and multiply them.
        """
        aim = 0
        horizontal = 0
        depth = 0

        for line in self.input_lines:
            command, value = line.split()
            value = int(value)

            if command == "forward":
                horizontal += value
                depth += aim * value
            elif command == "up":
                aim -= value
            elif command == "down":
                aim += value

        return horizontal * depth


