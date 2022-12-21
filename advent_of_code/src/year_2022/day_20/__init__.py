from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 0."""
    day = 0

    # example = True

    def part_1(self):
        """Run solution for part 1."""
        mixed = []
        zero_obj = None
        for line in self.input_lines:
            obj = {"num": int(line), "seen": False}
            if obj["num"] == 0:
                zero_obj = obj
            mixed.append(obj)

        length = len(mixed)
        i = 0
        count = 0
        while count < length:
            while mixed[i]["seen"]:
                i = (i + 1) % length
            obj = mixed.pop(i)
            obj["seen"] = True
            num = obj["num"]
            j = (i + num) % (length - 1)
            mixed.insert(j, obj)
            # print(f"{num} moves from {i} to {j}")
            if j <= i:
                i = (i + 1) % length
            count += 1
            # print([x["num"] for x in mixed])
            # print()

        # print([x["num"] for x in mixed])
        zero_idx = mixed.index(zero_obj)
        return sum(
            mixed[(zero_idx + delta) % length]["num"]
            for delta in (1000, 2000, 3000)
        )

    def part_2(self):
        """Run solution for part 2."""
        total = 0
        for line in self.input_lines:
            pass
        return total
