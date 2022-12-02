from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logic for solving day 1."""
    day = 1

    def part_1(self):
        """Find the Elf carrying the most Calories.
        How many total Calories is that Elf carrying?
        """
        highest = current = 0
        for cal_item in self.input_lines:
            if cal_item == "":
                if current > highest:
                    highest = current
                current = 0
            else:
                current += int(cal_item)

        if current > highest:
            highest = current

        return highest

    def part_2(self):
        """Find the top three Elves carrying the most Calories.
        How many Calories are those Elves carrying in total?
        """

        def update_highest(highest, current):
            for i in range(3):
                if current > highest[i]:
                    highest.insert(i, current)
                    highest.pop(3)
                    break

            return highest

        highest = [0, 0, 0]
        current = 0
        for cal_item in self.input_lines:
            if cal_item == "":
                highest = update_highest(highest, current)
                current = 0
            else:
                current += int(cal_item)

        highest = update_highest(highest, current)
        return sum(highest)
