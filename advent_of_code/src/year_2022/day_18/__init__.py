import re

from advent_of_code.src.constants import INFINITE
from advent_of_code.src.utils import BaseSolution

BLK = "#"
WTR = "~"
AIR = "."


class Solution(BaseSolution):
    """Logics for solving day 18."""
    day = 18
    highest_dim = 0
    cubes = []
    map = dict()
    x_ranges = dict()
    y_ranges = dict()
    z_ranges = dict()

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
            self.highest_dim = max(self.highest_dim, x, y, z)
            self.cubes.append((x, y, z))
            self.set_voxel(x, y, z)

    def part_1(self):
        """Find all sides of the glob."""
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

    def build_ranges(self):
        """Store highest and lowest values along each axis."""
        length = self.highest_dim
        for y in range(length):
            for z in range(length):
                low = INFINITE
                high = 0
                for x in self.map:
                    try:
                        item = self.map[x][y][z]
                    except KeyError:
                        continue
                    if not item:
                        continue
                    low = min(low, x)
                    high = max(high, x)
                if low and high:
                    key = str((y, z))
                    self.x_ranges[key] = low, high

        for x in range(length):
            for z in range(length):
                low = INFINITE
                high = 0
                for y in range(length):
                    try:
                        item = self.map[x][y][z]
                    except KeyError:
                        continue
                    if not item:
                        continue
                    low = min(low, y)
                    high = max(high, y)
                if low and high:
                    key = str((x, z))
                    self.y_ranges[key] = low, high

        for x in self.map:
            for y in range(length):
                key = str((x, y))
                try:
                    self.z_ranges[key] = min(self.map[x][y]), max(self.map[x][y])
                except KeyError:
                    continue

    def get_is_trapped(self, x, y, z):
        """Return True is air voxel and all connnect are trapped by blocks."""
        self.set_voxel(x, y, z, AIR)
        try:
            min_x, max_x = self.x_ranges[str((y, z))]
            min_y, max_y = self.y_ranges[str((x, z))]
            min_z, max_z = self.z_ranges[str((x, y))]
        except KeyError:
            # Out of known dimensions, must be exterior water
            self.set_voxel(x, y, z, WTR)
            return False

        if not min_x < x < max_x and min_y < y < max_y and min_z < z < max_z:
            # Out of range, must be exterior water
            self.set_voxel(x, y, z, WTR)
            return False

        for mod_x, mod_y, mod_z in self.SIDE_MODIFIERS:
            new_x = x + mod_x
            new_y = y + mod_y
            new_z = z + mod_z

            try:
                if self.map[new_x][new_y][new_z] in [BLK, AIR]:
                    # Wall or already checked, check next side
                    continue
                elif self.map[new_x][new_y][new_z] == WTR:
                    # Adjacent is known water, so this must also be
                    self.set_voxel(x, y, z, WTR)
                    return False
            except KeyError:
                pass
            if not self.get_is_trapped(new_x, new_y, new_z):
                # Some connection is known water, so this must also be
                self.set_voxel(x, y, z, WTR)
                return False

        # All connected air was checked so it must be trapped, consider block
        self.set_voxel(x, y, z, BLK)
        return True

    def part_2(self):
        """Find only exterior sides."""
        total = 0
        self.build_map()
        self.build_ranges()

        for cube_x, cube_y, cube_z in self.cubes:
            sides = 6
            for mod_x, mod_y, mod_z in self.SIDE_MODIFIERS:
                x = cube_x + mod_x
                y = cube_y + mod_y
                z = cube_z + mod_z

                try:
                    if self.map[x][y][z] == BLK:
                        sides -= 1
                        continue
                    elif self.map[x][y][z] == WTR:
                        # Exterior side, good to be counted
                        continue
                except KeyError:
                    pass

                # Check pocket of air
                if self.get_is_trapped(x, y, z):
                    sides -= 1

            total += sides

        return total  # 656 < ANSWER < 3214 | 3139 x
