from advent_of_code.src.utils import BaseSolution
import re

REGEX = re.compile(r"(\d+)")


class Solution(BaseSolution):
    """Logics for solving day 4."""
    day = 4
    colon_pos = 0
    pipe_pos = 0

    # example = True

    def set_values(self):
        self.colon_pos = self.input_lines[0].find(":")
        self.pipe_pos = self.input_lines[0].find("|")

    def get_winning_matches(self, line):
        winning_numbers = set(REGEX.findall(line[self.colon_pos:self.pipe_pos]))
        my_numbers = set(REGEX.findall(line[self.pipe_pos:]))
        return winning_numbers & my_numbers

    def part_1(self):
        """Return how many points the scratchcards are worth in total."""
        total = 0
        self.set_values()
        for line in self.input_lines:
            matches = self.get_winning_matches(line)
            if not matches:
                continue
            total += 2 ** (len(matches) - 1)
        return total

    def part_2(self):
        """Return how many total scratchcards do you end up with."""
        self.set_values()
        cards_count = [1 for x in range(len(self.input_lines))]
        length = len(self.input_lines) - 1
        for idx, line in enumerate(self.input_lines[::-1]):
            idx = length - idx
            n_matches = len(self.get_winning_matches(line))
            for next_idx in range(idx + 1, idx + n_matches + 1):
                cards_count[idx] += cards_count[next_idx]
        return sum(cards_count)
