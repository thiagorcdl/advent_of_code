from advent_of_code.src.utils import BaseSolution
import re


class Solution(BaseSolution):
    """Logics for solving day 5."""
    day = 5

    # example = True

    def part_1(self):
        """Return the lowest location number that corresponds to any of the
        initial seed numbers.
        """
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
        """Return the lowest location number that corresponds to any of the
        initial seed numbers.
        """
        targets = {
            (int(x[0]), int(x[1]))
            for x in re.findall(r"(\d+) (\d+)", self.input_lines[0])
        }

        sources = set()
        for line in self.input_lines[2:]:
            match = re.match(r"(\d+) (\d+) (\d+)", line)
            if not match:
                if ":" in line:
                    # New section
                    sources |= targets
                    targets = set()
                continue

            target_map_start = int(match.group(1))
            source_map_start = int(match.group(2))
            map_range = int(match.group(3))
            source_map_end = source_map_start + map_range

            # Apply mappings
            remainders, sources, targets = self.apply_mappings(
                sources, source_map_start, source_map_end,
                target_map_start, map_range, targets
            )
            while remainders:
                remainders, sources2, targets = self.apply_mappings(
                    remainders, source_map_start, source_map_end,
                    target_map_start, map_range, targets
                )
                sources |= sources2

        targets |= sources
        return min([t[0] for t in targets])

    def apply_mappings(
        self, sources, source_map_start, source_map_end,
        target_map_start, map_range, targets
    ):
        remainders = set()

        # Apply mappings
        for seed_group in [x for x in sources]:
            seed_group_start = seed_group[0]
            seed_group_range = seed_group[1]
            seed_group_end = seed_group_start + seed_group_range
            seed_offset = seed_group_start - source_map_start
            if (
                source_map_start <= seed_group_start
                and source_map_end >= seed_group_end
            ):
                # 1 - Source being mapped contains seed range
                result = (
                    target_map_start + seed_offset,
                    seed_group_range,
                )
            elif (
                source_map_start <= seed_group_start
                < source_map_end < seed_group_end
            ):
                # 2 - Source being mapped partially contains seed range (lower)
                result = (
                    target_map_start + seed_offset,
                    (source_map_start + map_range) - seed_group_start,
                )
                # Upper remainder
                remainder = (
                    source_map_end,
                    (seed_group_start + seed_group_range) - source_map_end,
                )
                remainders.add(remainder)
            elif (
                seed_group_start < source_map_start
                < seed_group_end <= source_map_end
            ):
                # 3 - Source being mapped partially contains seed range (upper)
                result = (
                    target_map_start,
                    (seed_group_start + seed_group_range) - source_map_start,
                )
                # Lower remainder
                remainder = (
                    seed_group_start,
                    source_map_start - seed_group_start,
                )
                remainders.add(remainder)
            elif (
                source_map_start > seed_group_start
                and source_map_end < seed_group_end
            ):
                # 4 - Source being mapped is contained seed range
                result = (
                    target_map_start,
                    map_range,
                )
                # Upper remainder
                remainder = (
                    source_map_end,
                    (seed_group_start + seed_group_range) - source_map_end,
                )
                remainders.add(remainder)
                # Lower remainder
                remainder = (
                    seed_group_start,
                    source_map_start - seed_group_start,
                )
                remainders.add(remainder)
            else:
                continue

            sources.remove(seed_group)
            targets.add(result)

        return remainders, sources, targets
