import re
from copy import copy
from functools import lru_cache
from math import ceil

from advent_of_code.src.utils import BaseSolution

ORE = "ore"
CLAY = "clay"
OBS = "obsidian"
GEO = "geode"
MATERIAL_TYPES = [ORE, CLAY, OBS, GEO]


class BotBase:
    materials: dict
    produces: str

    @classmethod
    def rate(cls):
        material_counts = list(cls.materials.values())
        return material_counts[0] / material_counts[1]


class OreBot(BotBase):
    materials = {ORE: 0}
    produces = ORE


class ClayBot(BotBase):
    materials = {ORE: 0}
    produces = CLAY


class ObsidianBot(BotBase):
    materials = {ORE: 0, CLAY: 0}
    produces = OBS


class GeodeBot(BotBase):
    materials = {ORE: 0, OBS: 0}
    produces = GEO


ROBOT_CLASSES = [OreBot, ClayBot, ObsidianBot, GeodeBot]


class Solution(BaseSolution):
    """Logics for solving day 19."""
    MEMOIZE = dict()
    MAX_MINUTE = 24
    PRODUCERS = {bot_class.produces: bot_class for bot_class in ROBOT_CLASSES}
    blueprints = []
    bp_max_geo = []
    robots = {bot_class: 0 for bot_class in ROBOT_CLASSES}
    materials = {mat_type: 0 for mat_type in MATERIAL_TYPES}
    assembly = []
    day = 19

    example = True

    def load_blueprints(self):
        """Read input."""
        for line in self.input_lines:
            bp = {bot_class: dict() for bot_class in ROBOT_CLASSES}
            ore = re.findall(r"Each ore robot costs (\d+) ore", line)[0]
            bp[OreBot][ORE] = int(ore)
            clay = re.findall(r"Each clay robot costs (\d+) ore", line)[0]
            bp[ClayBot][ORE] = int(clay)
            obs = re.findall(r"Each obsidian robot costs (\d+) ore and (\d+)", line)[0]
            bp[ObsidianBot][ORE] = int(obs[0])
            bp[ObsidianBot][CLAY] = int(obs[1])
            geo = re.findall(r"Each geode robot costs (\d+) ore and (\d+)", line)[0]
            bp[GeodeBot][ORE] = int(geo[0])
            bp[GeodeBot][OBS] = int(geo[1])
            self.blueprints.append(bp)
        # # print(self.blueprints)

    def get_quality_level(self, bp_id):
        return (bp_id + 1) * self.bp_max_geo[bp_id]

    def can_build(self, bot_class: BotBase, materials):
        """Check if there are enough materials to build bot."""
        for mat_type, mat_cost in bot_class.materials.items():
            if materials[mat_type] < mat_cost:
                return False
        return True

    def build(self, bot_class: BotBase, robots, materials):
        """Consume materials and add bot to assembly line."""
        robots = copy(robots)
        materials = copy(materials)
        for mat_type, mat_cost in bot_class.materials.items():
            materials[mat_type] -= mat_cost
        robots[bot_class] += 1
        return robots, materials

    def simulate(self, robots, materials, time_left):
        """Decide what to do next."""
        memoize_key = "".join([str(robots), str(materials), str(time_left)])
        if memoize_key in self.MEMOIZE:
            return self.MEMOIZE[memoize_key]
        # print(f"time: {self.MAX_MINUTE - time_left +1 } -------------------------------------------------")
        # print(f"robots {robots}")
        # print(f"materials {materials}")

        if time_left == 1:
            return 0

        max_ore_cost = max(bot.materials[ORE] for bot in ROBOT_CLASSES)
        predicted_usages = dict()
        predicted_usages[ORE] = int(ceil(
            (max_ore_cost * time_left - materials[ORE]) / time_left
        ))
        predicted_usages[CLAY] = int(ceil(
            (ObsidianBot.materials[CLAY] * time_left - materials[CLAY]) / time_left
        ))
        predicted_usages[OBS] = int(ceil(
            (GeodeBot.materials[OBS] * time_left - materials[OBS]) / time_left
        ))
        # print(f"\tpredicted_usages {predicted_usages}")
        missing_materials = [
            mat_type for mat_type, usage in predicted_usages.items()
            if usage > robots[self.PRODUCERS[mat_type]]
        ]
        # print(f"\tmissing_materials {missing_materials}")

        to_build = []
        if self.can_build(GeodeBot, materials):
            to_build.append(GeodeBot)
        if OBS in missing_materials:
            if self.can_build(ObsidianBot, materials):
                to_build.append(ObsidianBot)
            if self.can_build(ClayBot, materials) and CLAY in missing_materials:
                to_build.append(ClayBot)
        if self.can_build(OreBot, materials) and ORE in missing_materials:
            to_build.append(OreBot)
        # print(f"\tto_build {to_build}")

        # Gather materials
        for bot_class, count in robots.items():
            mat_type = bot_class.produces
            materials[mat_type] += count
            # print(f"\tCollect {count} {mat_type}")

        # Try building and see what happens
        max_geo = 0
        new_time_left = time_left - 1
        if to_build in [[], [ClayBot]]:
            max_geo = max(
                max_geo, self.simulate(robots, materials, new_time_left)
            )
        while to_build:
            bot_class = to_build.pop()
            # print(f"\t\tBuild robot: {bot_class}")
            new_robots, new_materials = self.build(bot_class, robots, materials)
            new_max = self.simulate(new_robots, new_materials, new_time_left)
            if bot_class == GeodeBot:
                new_max += new_time_left - 1
            max_geo = max(max_geo, new_max)
            if bot_class in [GeodeBot, ObsidianBot]:
                break
        self.MEMOIZE[memoize_key] = max_geo
        return max_geo

    def part_1(self):
        """Add up the quality level of all of the blueprints."""
        self.load_blueprints()
        for bp in self.blueprints:
            # print("#"*100)
            # print("#"*100)
            # print("#"*100)
            self.MEMOIZE = dict()
            for bot_class, materials in bp.items():
                bot_class.materials = materials
            self.materials = {mat_type: 0 for mat_type in MATERIAL_TYPES}
            self.assembly = []
            self.robots = {bot_class: 0 for bot_class in ROBOT_CLASSES}
            self.robots[OreBot] = 1

            result = self.simulate(self.robots, self.materials, self.MAX_MINUTE)
            self.bp_max_geo.append(result)

        print(self.bp_max_geo)
        return sum([
            self.get_quality_level(bp_id)
            for bp_id in range(len(self.blueprints))
        ])

    def part_2(self):
        """Run solution for part 2."""
        total = 0
        for line in self.input_lines:
            pass
        return total
