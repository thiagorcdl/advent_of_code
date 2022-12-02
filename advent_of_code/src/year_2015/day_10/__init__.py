from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 10."""
    day = 10

    def solve(self, part2=False):
        input_sequence = self.input_lines[0]

        def look(sequence):
            i = 0
            say = ''
            char = 0
            for i, c in enumerate(sequence):
                if c != sequence[char]:
                    say += str(i - char) + sequence[char]
                    char = i
            say += str(i - char + 1) + sequence[char]
            return say

        for n in range(50 if part2 else 40):
            input_sequence = look(input_sequence)
        return len(input_sequence)

    def part_1(self):
        """Run solution for part 1."""
        return self.solve()

    def part_2(self):
        """Run solution for part 2."""
        return self.solve(part2=True)
