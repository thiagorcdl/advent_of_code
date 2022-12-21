from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 20."""
    day = 20
    DEC_KEY = 811589153

    # example = True

    def solve(self, decription_key=1, iterations=1):
        order = []
        mixed = []
        zero_obj = None
        for idx, line in enumerate(self.input_lines):
            obj = {"num": int(line) * decription_key, "id": idx}
            if obj["num"] == 0:
                zero_obj = obj
            order.append(obj)
            mixed.append(obj)

        length = len(mixed)
        for turn in range(iterations):
            for obj in order:
                i = mixed.index(obj)
                obj = mixed.pop(i)
                j = (i + obj["num"]) % (length - 1)
                mixed.insert(j, obj)

        zero_idx = mixed.index(zero_obj)
        return sum(
            mixed[(zero_idx + delta) % length]["num"]
            for delta in (1000, 2000, 3000)
        )

    def part_1(self):
        """Run solution for part 1."""
        return self.solve()

    def part_2(self):
        """Run solution for part 2."""
        return self.solve(811589153, 10)
