#!/usr/bin/env python

class BaseResolution:
    """Base class to be used by each day."""
    day = 0

    @staticmethod
    def part_1(input_lines: list):
        """Run solution for part 1."""
        raise NotImplementedError

    @staticmethod
    def part_2(input_lines: list):
        """Run solution for part 2."""
        raise NotImplementedError

    @classmethod
    def run(cls, part: int, input_lines: list):
        """Execute the method corresponding to the specified part."""
        method_map = {
            1: cls.part_1,
            2: cls.part_2,
        }
        method = method_map[part]
        return method(input_lines)
