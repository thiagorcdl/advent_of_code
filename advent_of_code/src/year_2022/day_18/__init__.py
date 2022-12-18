import re

from advent_of_code.src.utils import BaseSolution

BLK = "#"


class Solution(BaseSolution):
    """Logics for solving day 18."""
    day = 18
    highest_dim = 0
    cubes = []
    map = dict()

    # example = True

    def build_map(self):
        for line in self.input_lines:
            try:
                x, y, z = [int(x) for x in re.findall(r"(\d+)", line)]
            except:
                continue
            self.highest_dim = max(self.highest_dim, x, y, z)
            self.cubes.append((x, y, z))

            try:
                x_axis = self.map[x]
            except KeyError:
                self.map[x] = {y: {z: BLK}}
                continue
            try:
                y_axis = x_axis[y]
            except KeyError:
                x_axis[y] = {z: BLK}
                continue
            y_axis[z] = BLK

    def part_1(self):
        """Find all sides of the glob."""
        total = 0
        self.build_map()
        mods = [
            (0, 0, 1),
            (0, 0, -1),
            (0, 1, 0),
            (0, -1, 0),
            (1, 0, 0),
            (-1, 0, 0),
        ]

        for cube_x, cube_y, cube_z in self.cubes:
            sides = 6
            for mod_x, mod_y, mod_z in mods:
                x = cube_x + mod_x
                y = cube_y + mod_y
                z = cube_z + mod_z

                try:
                    if self.map[x][y][z]:
                        sides -= 1
                except KeyError:
                    continue
            total += sides

        return total

    def part_2(self):
        """Find only exterior sides."""
        total = 0
        for line in self.input_lines:
            pass
        return total
