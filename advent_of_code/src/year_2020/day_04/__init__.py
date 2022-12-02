#!/usr/bin/env python
import re
from advent_of_code.src.utils import BaseResolution

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

    def part_1(self):
        """Run solution for part 1."""
        total = 0
        fields = set()
        for line in self.input_lines:
            if not line.strip():
                if fields >= REQUIRED:
                    total += 1
                fields = set()
                continue

            matches = re.findall(r"(byr|iyr|eyr|hgt|hcl|ecl|pid):", line)
            fields |= set(matches)

        if fields >= REQUIRED:
            total += 1
        return total

    def validate_byr(self, value) -> bool:
        """Return True if four digits; at least 1920 and at most 2002."""
        return re.match(r"\d{4}$", value) and 1920 <= int(value) <= 2002

    def validate_iyr(self, value) -> bool:
        """Return True if four digits; at least 2010 and at most 2020."""
        return re.match(r"\d{4}$", value) and 2010 <= int(value) <= 2020

    def validate_eyr(self, value) -> bool:
        """Return True if four digits; at least 2020 and at most 2030."""
        return re.match(r"\d{4}$", value) and 2020 <= int(value) <= 2030

    def validate_hgt(self, value) -> bool:
        """Return True if a number followed by either cm or in:
            - If cm, the number must be at least 150 and at most 193.
            - If in, the number must be at least 59 and at most 76.
        """
        match = re.match(r"(\d+)(\w+)$", value)
        if not match:
            return False
        height = int(match.group(1))
        unit = match.group(2)
        if unit == "cm":
            return 150 <= height <= 193
        if unit == "in":
            return 59 <= height <= 76
        return False

    def validate_hcl(self, value) -> bool:
        """Return True if a # followed by exactly six characters 0-9 or a-f."""
        return bool(re.match(r"#[0-9a-f]{6}$", value))

    def validate_ecl(self, value) -> bool:
        """Return True if exactly one of: amb blu brn gry grn hzl oth."""
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def validate_pid(self, value) -> bool:
        """Return True if a nine-digit number, including leading zeroes."""
        return bool(re.match(r"\d{9}$", value))

    def call_validator(self, field, value):
        """Run appropriate validator for field."""
        return eval(f"self.validate_{field}(value)")

    def validate(self, fields):
        """Run all validations for fields."""
        fieldset = set([x[0] for x in fields])
        return fieldset >= REQUIRED and all([
            self.call_validator(field, value)
            for field, value in fields
        ])

    def part_2(self):
        """Run solution for part 2."""
        total = 0
        fields = []
        for line in self.input_lines:
            if not line.strip():
                if self.validate(fields):
                    total += 1
                fields = []
                continue

            matches = re.findall(
                r"(byr|iyr|eyr|hgt|hcl|ecl|pid):(#?\w+)", line
            )
            fields.extend(matches)

        if self.validate(fields):
            total += 1
        return total
