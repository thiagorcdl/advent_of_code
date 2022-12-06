from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 6."""
    day = 6

    def solve(self, buffer_size=4):
        """Find the position where the buffer is filled with unique chars."""
        stream = self.input_lines[0]
        buffer = list(stream[:buffer_size])
        idx = buffer_size
        while len(set(buffer)) < buffer_size and idx < len(stream):
            buffer.append(stream[idx])
            buffer.pop(0)
            idx += 1
        return idx

    def part_1(self):
        """Find the position where there are 4 unique chars."""
        return self.solve()

    def part_2(self):
        """Find the position where there are 14 unique chars."""
        return self.solve(buffer_size=14)


