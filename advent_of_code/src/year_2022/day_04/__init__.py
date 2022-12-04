from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 4."""
    day = 4

    def get_set(self, assignment: str) -> set:
        start, end = map(int, assignment.split('-'))
        return {x for x in range(start, end + 1)}

    def part_1(self):
        """Find how many assignment pairs does one range fully contain the other."""
        total = 0

        for line in self.input_lines:
            first, second = line.split(',')
            first_set = self.get_set(first)
            second_set = self.get_set(second)
            if first_set.issubset(second_set) or second_set.issubset(first_set):
                total += 1
        return total

    def part_2(self):
        """Find how many assignment pairs do the ranges overlap."""
        total = 0
        for line in self.input_lines:
            first, second = line.split(',')
            first_set = self.get_set(first)
            second_set = self.get_set(second)
            if first_set & second_set:
                total += 1
        return total
