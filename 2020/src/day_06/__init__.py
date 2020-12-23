#!/usr/bin/env python
import re

from string import ascii_lowercase
from src.utils import BaseResolution


class Resolution(BaseResolution):
    """Logics for resolving day 6."""
    day = 6

    def part_1(self, input_lines: list):
        """Count the number of questions to which anyone answered "yes"."""
        total = 0
        questions = set()
        for line in input_lines:
            if not line.strip():
                total += len(questions)
                questions = set()
                continue

            matches = re.findall(r"[a-z]", line)
            questions |= set(matches)

        total += len(questions)
        print(total)

    def part_2(self, input_lines: list):
        """Count the number of questions to which EVERYONE answered "yes"."""
        total = 0
        questions = set(ascii_lowercase)
        for line in input_lines:
            if not line.strip():
                total += len(questions)
                questions = set(ascii_lowercase)
                continue

            matches = re.findall(r"[a-z]", line)
            questions &= set(matches)

        total += len(questions)
        print(total)
