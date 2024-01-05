from advent_of_code.src.utils import BaseSolution
import re
SEED_SOIL_MAP = dict()
SOIL_FERT_MAP = dict()
FERT_WATER_MAP = dict()
WATER_LIGHT_MAP = dict()
LIGHT_TEMP_MAP = dict()
TEMP_HUM_MAP = dict()
HUM_LOC_MAP = dict()

MAPS = {
    "seed-to-soil": SEED_SOIL_MAP,
    "soil-to-fertilizer": SOIL_FERT_MAP,
    "fertilizer-to-water": FERT_WATER_MAP,
    "water-to-light": WATER_LIGHT_MAP,
    "light-to-temperature": LIGHT_TEMP_MAP,
    "temperature-to-humidity": TEMP_HUM_MAP,
    "humidity-to-location": HUM_LOC_MAP,
}

MAP_NAMES = list(MAPS.keys())


class Solution(BaseSolution):
    """Logics for solving day 5."""
    day = 5
    curr_map_idx = -1
    curr_map_name = ""
    curr_map = None

    # example = True

    def iter_map(self):
        self.curr_map_idx += 1
        self.curr_map_name = MAP_NAMES[self.curr_map_idx]
        self.curr_map = MAPS[self.curr_map_name]

    def part_1(self):
        """Run solution for part 1."""
        targets = [int(x) for x in re.findall(r"(\d+)", self.input_lines[0])]
        sources = [x for x in targets]

        for line in self.input_lines[3:]:
            match = re.match(r"(\d+) (\d+) (\d+)", line)
            if not match:
                # New section
                sources = [x for x in targets]
                continue

            target_start = int(match.group(1))
            source_start = int(match.group(2))
            map_range = int(match.group(3))

            # Apply mappings
            for idx, seed in enumerate(sources):
                if not source_start <= seed < source_start + map_range:
                    continue

                seed_offset = seed - source_start
                targets[idx] = target_start + seed_offset

        return min(targets)

    def part_2(self):
        """Run solution for part 2."""
        total = 0
        for line in self.input_lines:
            pass
        return total
