#!/usr/bin/env python

class BaseResolution:
    """Base class to be used by each day."""
    day = 0

    def part_1(self, input_lines: list):
        """Run solution for part 1."""
        raise NotImplementedError

    def part_2(self, input_lines: list):
        """Run solution for part 2."""
        raise NotImplementedError

    def run(self, part: int, input_lines: list):
        """Execute the method corresponding to the specified part."""
        method_map = {
            1: self.part_1,
            2: self.part_2,
        }
        method = method_map[part]
        return method(input_lines)
