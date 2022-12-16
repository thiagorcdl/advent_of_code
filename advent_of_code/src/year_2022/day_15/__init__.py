import re
from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 15."""
    day = 15
    beacons = set()
    non_beacon = dict()
    MAX = 4000000
    # example = True

    def mark_non_beacon(self, coord_x, coord_y):
        """Add coordinates to the the map of cleared spaces."""
        coord_str = str((coord_x, coord_y))
        try:
            self.non_beacon[coord_y].add(coord_str)
        except KeyError:
            self.non_beacon[coord_y] = {coord_str}

    def build_map(self, row=2000000):
        """Read input data of sensors and beacons."""
        for line in self.input_lines:
            sensor_x, sensor_y, beacon_x, beacon_y = [
                int(x) for x in re.findall(r"=(-?\d+)", line)
            ]
            self.mark_non_beacon(sensor_x, sensor_y)
            self.beacons.add(str((beacon_x, beacon_y)))
            cover_range = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
            row_dist = abs(sensor_y - row)
            tree_height = cover_range - (row_dist - 1)
            if tree_height > 0:
                tree_line_size = 1 + 2 * (tree_height - 1)
                half = tree_line_size // 2
                for col in range(sensor_x - half, sensor_x + half + 1):
                    self.mark_non_beacon(col, row)

    def part_1(self):
        """Find how many positions cannot contain a beacon in row 2000000."""
        row = 10 if self.example else 2000000
        self.build_map(row=row)
        return len(self.non_beacon[row] - self.beacons)

    def add_range(self, row: dict, start, end):
        """Add range to row, and merge if possible."""
        if row["complete"]:
            return

        i = 0
        while i < len(row["ranges"]):
            existing = row["ranges"][i]
            merged = False
            if existing[0] < start <= existing[1]:
                start = existing[0]
                merged = True
            elif start < existing[0] <= end:
                merged = True

            if existing[0] <= end < existing[1]:
                end = existing[1]
                merged = True
            elif start <= existing[1] < end:
                merged = True
            if merged:
                row["ranges"].pop(i)
                i = 0
            else:
                i += 1
        row["ranges"].append((start, end))

        max_col = 20 if self.example else self.MAX
        total = 0
        for existing in row["ranges"]:
            total += (existing[1] - existing[0]) + 1
        if total == max_col + 1:
            row["complete"] = True
            # row["ranges"] = None

    def find_missing_col(self, ranges):
        """Find the missing in x axis."""
        ranges.sort(key=lambda x: x[0])
        next_number = 0
        for start, end in ranges:
            if next_number < start:
                return next_number
            next_number = end + 1
        return None

    def part_2(self):
        """Run solution for part 2."""
        rows = [{"complete": False, "ranges": []} for i in range(self.MAX)]

        for line in self.input_lines:
            sensor_x, sensor_y, beacon_x, beacon_y = [
                int(x) for x in re.findall(r"=(-?\d+)", line)
            ]
            cover_range = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)

            yrange_start = max(sensor_y - cover_range, 0)
            yrange_end = min(sensor_y + cover_range + 1, self.MAX)
            for row in range(yrange_start, yrange_end):
                row_dist = abs(sensor_y - row)
                tree_height = cover_range - (row_dist - 1)
                if tree_height <= 0:
                    continue

                tree_line_size = 1 + 2 * (tree_height - 1)
                half = tree_line_size // 2
                xrange_start = max(sensor_x - half, 0)
                xrange_end = min(sensor_x + half, self.MAX)
                self.add_range(rows[row], xrange_start, xrange_end)

        y = x = None
        for i, row in enumerate(rows):
            if row["complete"]:
                continue
            y = i
            x = self.find_missing_col(row["ranges"])
            if x is not None:
                break

        if None in (x, y):
            return
        return x * 4000000 + y
