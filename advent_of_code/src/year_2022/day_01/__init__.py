from advent_of_code.src.utils import BaseResolution


class Resolution(BaseResolution):
    """Logic for resolving day 1."""
    day = 1

    def part_1(self):
        """Print the highest amount of calories carried by an elf."""
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
        """TODO"""
        pass
