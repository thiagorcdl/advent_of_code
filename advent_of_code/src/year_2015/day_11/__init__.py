import re

from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 11."""
    day = 11

    def solve(self, part2=False):
        str_pwd = self.input_lines[0]
        pwd = list(map(ord, list(str_pwd)))

        def incr(ch):
            return 97 + ((ch - 96) % 26)

        for i, char in enumerate(str_pwd):
            if char in ['i', 'o', 'l']:
                pwd[i] = incr(pwd[i])
                for j in range(i + 1, 8):
                    pwd[j] = 97
                str_pwd = "".join(map(chr, pwd))
                break

        def find_next(pwd):
            while True:
                for i, char in enumerate(reversed(pwd)):
                    j = -(i + 1)
                    # Base is 97 ('a'); uses mod 26 for the offset
                    pwd[j] = 97 + ((char - 96) % 26)
                    if pwd[j] in ['i', 'o', 'l']:
                        # Jumps to next acceptable string | fiaa -> fjaa
                        pwd[j] = incr(pwd[i])
                    if pwd[j] != 97:
                        break
                has_seq = False
                for i, char in enumerate(pwd):
                    if i == len(pwd) - 2:
                        break
                    if pwd[i + 1] == pwd[i] + 1 and pwd[i + 2] == pwd[i] + 2:
                        has_seq = True
                str_pwd = "".join(map(chr, pwd))
                n_pairs = len(set(re.findall(r'(\w)\1', str_pwd)))
                if n_pairs > 1 and has_seq:
                    break
            return str_pwd

        next_pwd = find_next(pwd)
        if part2:
            next_pwd = find_next(list(map(ord, list(next_pwd))))
        return next_pwd

    def part_1(self):
        """Run solution for part 1."""
        return self.solve()

    def part_2(self):
        """Run solution for part 2."""
        return self.solve(part2=True)

