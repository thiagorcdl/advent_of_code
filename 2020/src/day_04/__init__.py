#!/usr/bin/env python
import re
from src.utils import BaseResolution

REQUIRED = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
}


class Resolution(BaseResolution):
    """Logics for resolving day 4."""
    day = 4

    def part_1(self, input_lines: list):
        """Run solution for part 1."""
        total = 0
        fields = set()
        for line in input_lines:
            if not line.strip():
                if fields >= REQUIRED:
                    total += 1
                fields = set()
                continue

            matches = re.findall(r"(byr|iyr|eyr|hgt|hcl|ecl|pid):", line)
            fields |= set(matches)

        if fields >= REQUIRED:
            total += 1
        print(total)
