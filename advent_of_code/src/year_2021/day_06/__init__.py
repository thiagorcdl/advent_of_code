#!/usr/bin/env python
from functools import lru_cache

from advent_of_code.src.utils import BaseResolution

FISH_CYCLE_DAYS = 7
EXISTING_FISH_START = 6
NEW_FISH_START = 8
MAX_DAYS1 = 80
MAX_DAYS2 = 256


class Resolution(BaseResolution):
    """Logics for resolving day 6."""
    day = 6

    init_cache = {}

    def part_1(self):
        """Run brute-force solution to find out how many lanternfish would there be
        after 80 days.
        """
        line = self.input_lines[0]

        existing_fish = [int(x) for x in line.split(",")]
        total = len(existing_fish)

        for day in range(MAX_DAYS1):
            new_fish = []
            for idx in range(total):
                if existing_fish[idx] == 0:
                    existing_fish[idx] = EXISTING_FISH_START
                    new_fish.append(NEW_FISH_START)
                else:
                    existing_fish[idx] -= 1

            existing_fish += new_fish
            total = len(existing_fish)
        print(total)

    @lru_cache(40960)
    def get_children(self, start_timer, max_days) -> int:
        """Calculate a fish's amount of direct children."""
        offset = EXISTING_FISH_START - start_timer
        result = (max_days + offset) // FISH_CYCLE_DAYS
        return result

    @lru_cache(20480)
    def recursive_get_family(self, fish, max_days) -> int:
        """Get amount children's children recursively until the last day."""
        total = 0
        if max_days < 0:
            return total

        total += self.get_children(fish, max_days)
        for n_child in range(total):
            total += self.recursive_get_family(
                0,
                max_days - n_child * FISH_CYCLE_DAYS - EXISTING_FISH_START * 2,
            )

        return total

    def part_2(self):
        """Run faster solution for 256 days (WIP)."""
        line = self.input_lines[0]

        existing_fish = [int(x) for x in line.split(",")]
        total = len(existing_fish)
        print(f"Start total: {total}")

        for fish in existing_fish:
            # Calculate this fish's family growth
            print("----------\n")
            print(f"Calculating for timer {fish}")

            labour_day = fish + 1
            try:
                result = self.init_cache[fish]
                print(f"\tgrabbed from cache: {result}")
            except KeyError:
                # Fish not in cache yet
                result = self.get_children(fish, MAX_DAYS2)

                for n_child in range(total):
                    result += self.recursive_get_family(
                        NEW_FISH_START,
                        MAX_DAYS2 - labour_day - n_child * FISH_CYCLE_DAYS,
                    )

                self.init_cache[fish] = result
                print(f"\tresult for {fish}: {result}")

            total += result
            print(self.init_cache)

            print(f"total: {total}")

        print(total)

# 173078835695
