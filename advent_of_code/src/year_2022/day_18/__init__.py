import re

from advent_of_code.src.constants import INFINITE
from advent_of_code.src.utils import BaseSolution

BLK = "#"


class Solution(BaseSolution):
    """Logics for solving day 18."""
    day = 18
    cubes = []
    cubes2 = set()
    map = dict()
    x_range = [INFINITE, 0]
    y_range = [INFINITE, 0]
    z_range = [INFINITE, 0]

    SIDE_MODIFIERS = [
        (0, 0, 1),
        (0, 0, -1),
        (0, 1, 0),
        (0, -1, 0),
        (1, 0, 0),
        (-1, 0, 0),
    ]

    # example = True

    def set_voxel(self, x, y, z, value=BLK):
        """Assign value to specified coordinates."""
        try:
            x_axis = self.map[x]
        except KeyError:
            self.map[x] = {y: {z: value}}
            return
        try:
            y_axis = x_axis[y]
        except KeyError:
            x_axis[y] = {z: value}
            return
        y_axis[z] = value

    def build_map(self):
        """Read input and set values."""
        for line in self.input_lines:
            try:
                x, y, z = [int(x) for x in re.findall(r"(\d+)", line)]
            except:
                continue
            self.x_range = min(self.x_range[0], x - 1), max(self.x_range[1], x + 1)
            self.y_range = min(self.y_range[0], y - 1), max(self.y_range[1], y + 1)
            self.z_range = min(self.z_range[0], z - 1), max(self.z_range[1], z + 1)
            self.cubes.append((x, y, z))
            self.cubes2.add(str((x, y, z)))
            self.set_voxel(x, y, z)

    def part_1(self):
        """Find all sides of the rock."""
        total = 0
        self.build_map()

        for cube_x, cube_y, cube_z in self.cubes:
            sides = 6
            for mod_x, mod_y, mod_z in self.SIDE_MODIFIERS:
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

    def in_range(self, x, y, z):
        return (
            self.x_range[0] <= x <= self.x_range[1]
            and self.y_range[0] <= y <= self.y_range[1]
            and self.z_range[0] <= z <= self.z_range[1]
        )

    def part_2(self):
        """Find only exterior sides."""
        total = 0
        self.build_map()

        air_queue = [(self.x_range[0], self.y_range[0], self.z_range[0],)]
        visited = set()

        while air_queue:
            air_point = air_queue.pop(0)
            air_key = str(air_point)
            if air_key in visited:
                continue

            visited.add(air_key)
            air_x, air_y, air_z = air_point
            for mod_x, mod_y, mod_z in self.SIDE_MODIFIERS:
                x = air_x + mod_x
                y = air_y + mod_y
                z = air_z + mod_z
                point = (x, y, z)

                if not self.in_range(x, y, z):
                    continue

                if str(point) in self.cubes2:
                    total += 1
                else:
                    air_queue.append(point)

        return total  # 656 < ANSWER < 3214 | 3139 x
