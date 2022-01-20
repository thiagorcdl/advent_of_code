#!/usr/bin/env python
from advent_of_code.src.utils import BaseResolution
import re
from operator import add, sub

OPERATORS = {"+": add, "-": sub}


class Resolution(BaseResolution):
    """Logics for resolving day 8."""
    day = 8

    def part_1(self):
        """Find what value is in the accumulator."""
        acc = 0
        visited = []
        i = 0
        while i not in visited:
            visited.append(i)
            match = re.match(r"(nop|acc|jmp) (\+|-)(\d+)", input_lines[i])
            cmd = match.group(1)
            operator = OPERATORS[match.group(2)]
            param = int(match.group(3))

            if cmd == "jmp":
                i = operator(i, param)
            else:
                i += 1
            if cmd == "acc":
                acc = operator(acc, param)

        print(acc)

    def run_program(self):
        """Run all instructions and check whether end was achieved."""
        acc = 0
        visited = []
        i = 0
        while i < len(self.input_lines):
            if i in visited:
                return False, acc
            visited.append(i)
            match = re.match(r"(nop|acc|jmp) (\+|-)(\d+)", input_lines[i])
            cmd = match.group(1)
            operator = OPERATORS[match.group(2)]
            param = int(match.group(3))

            if cmd == "jmp":
                i = operator(i, param)
            else:
                i += 1
            if cmd == "acc":
                acc = operator(acc, param)
        return True, acc

    def part_2(self):
        """Fix the program so that it terminates normally by changing
        exactly one jmp (to nop) or nop (to jmp).

        What is the value of the accumulator after the program terminates?
        """
        visited = []
        i = 0
        jmp_idx = set()
        nop_idx = set()
        while i < len(self.input_lines):
            if i in visited:
                for idx in jmp_idx:
                    input_lines[idx] = input_lines[idx].replace("jmp", "nop")
                    success, acc = self.run_program()
                    if success:
                        print(acc)
                        return
                    input_lines[idx] = input_lines[idx].replace("nop", "jmp")

                for idx in nop_idx:
                    input_lines[idx] = input_lines[idx].replace("nop", "jmp")
                    success, acc = self.run_program()
                    if success:
                        print(acc)
                        return
                    input_lines[idx] = input_lines[idx].replace("jmp", "nop")

                print("FAILED repeating", i)
                return

            visited.append(i)
            match = re.match(r"(nop|acc|jmp) (\+|-)(\d+)", input_lines[i])
            cmd = match.group(1)
            operator = OPERATORS[match.group(2)]
            param = int(match.group(3))

            if cmd == "nop":
                nop_idx.add(i)
            if cmd == "jmp":
                jmp_idx.add(i)
                i = operator(i, param)
            else:
                i += 1
