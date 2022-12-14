from functools import cmp_to_key

from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 13."""
    day = 13
    DIV_PACKS = [
        [[2]],
        [[6]],
    ]

    # example = True

    def is_correct(self, left: list, right: list):
        """Compare pairs to see if left is lower or ends first."""
        if not isinstance(left, list):
            left = [left]
        elif not isinstance(right, list):
            right = [right]

        if right and not left:
            return -1
        elif left and not right:
            return 1

        for i in range(len(left)):
            try:
                item_left = left[i]
            except IndexError:
                return -1
            try:
                item_right = right[i]
            except IndexError:
                return 1

            if isinstance(item_left, list) or isinstance(item_right, list):
                result = self.is_correct(item_left, item_right)
                if result is not None:
                    return result
            elif item_left < item_right:
                return -1
            elif item_right < item_left:
                return 1
        if len(left) < len(right):
            return -1

    def part_1(self):
        """Return the sum of the indices of the correct pairs."""
        total = 0
        idx = 1
        for i in range(0, len(self.input_lines), 3):
            left_raw, right_raw = self.input_lines[i:i + 2]
            left = eval(left_raw)
            right = eval(right_raw)
            if self.is_correct(left, right) == -1:
                total += idx
            idx += 1
        return total

    def part_2(self):
        """Find the indices of the additional packages and multiply them."""
        pack_list = [self.DIV_PACKS[0], self.DIV_PACKS[1]]
        for i in range(0, len(self.input_lines), 3):
            left_raw, right_raw = self.input_lines[i:i + 2]
            left = eval(left_raw)
            right = eval(right_raw)
            pack_list.append(left)
            pack_list.append(right)

        pack_list.sort(key=cmp_to_key(self.is_correct))
        idx1 = pack_list.index(self.DIV_PACKS[0]) +1
        idx2 = pack_list.index(self.DIV_PACKS[1]) +1
        return  idx1*idx2
