import re

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
    MAX_MINUTE = 24
    PRODUCERS = {bot_class.produces: bot_class for bot_class in ROBOT_CLASSES}
    seeking_material = None
    blueprints = []
    bp_max_geo = []
    robots = {bot_class: 0 for bot_class in ROBOT_CLASSES}
    materials = {mat_type: 0 for mat_type in MATERIAL_TYPES}
    assembly = []
    day = 19

    example = True

    def get_quality_level(self, bp_id):
        return (bp_id + 1) * self.bp_max_geo[bp_id]

    def get_missing_materials(self, bot_class: BotBase):
        """Check if there are enough materials to build bot."""
        missing = []
        for mat_type, mat_cost in bot_class.materials.items():
            if self.materials[mat_type] < mat_cost:
                missing.append(mat_type)
        return missing

    def build(self, bot_class: BotBase):
        """Consume materials and add bot to assembly line."""
        for mat_type, mat_cost in bot_class.materials.items():
            self.materials[mat_type] -= mat_cost
        self.assembly.append(bot_class)

    def try_build(self):
        bot_class = self.PRODUCERS[self.seeking_material]
        print(f"try_build bot_class: {bot_class}")

        missing_materials = self.get_missing_materials(bot_class)
        if not missing_materials:
            self.seeking_material = None
            self.build(bot_class)
            print(f"\tSuccess {bot_class}")
            return True

        if len(missing_materials) == 1:
            self.seeking_material = missing_materials[0]
        else:
            # Decide which one to prioritize
            producer1 = self.PRODUCERS[missing_materials[0]]
            producer2 = self.PRODUCERS[missing_materials[1]]
            try:
                production_rate = self.robots[producer1] / self.robots[producer2]
            except ZeroDivisionError:
                production_rate = 999

            bot_rate = bot_class.rate()
            if bot_rate > production_rate:
                # Bot requires more abundance of mat0
                self.seeking_material = missing_materials[0]
            elif bot_rate < production_rate:
                # Bot requires more abundance of mat1
                self.seeking_material = missing_materials[1]

        if self.PRODUCERS[self.seeking_material] == bot_class:
            self.seeking_material = None
        return False

    def simulate(self):
        """Decide what to do next.

        Proportion -> mat0 / mat1 # bigger means abudance of mat0
        """
        while self.seeking_material and not self.try_build():
            print(f"seeking_material: {self.seeking_material}")
            continue
        for bot_class, count in self.robots.items():
            mat_type = bot_class.produces
            self.materials[mat_type] += count
            print(f"Collect {count} {mat_type}")
        if self.assembly:
            print(f"Build robot: {bot_class}")
            bot_class = self.assembly.pop()
            self.robots[bot_class] += 1

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
        # print(self.blueprints)

    def part_1(self):
        """Add up the quality level of all of the blueprints."""
        self.load_blueprints()
        for bp in self.blueprints:
            print("#"*100)
            print("#"*100)
            print("#"*100)
            for bot_class, materials in bp.items():
                bot_class.materials = materials
            self.materials = {mat_type: 0 for mat_type in MATERIAL_TYPES}
            self.assembly = []
            self.robots = {bot_class: 0 for bot_class in ROBOT_CLASSES}
            self.robots[OreBot] = 1

            for minute in range(self.MAX_MINUTE):
                print("="*80)
                print(f"minute: {minute}")
                self.seeking_material = GEO
                self.simulate()
                print(f"materials: {self.materials}")

            self.bp_max_geo.append(self.materials[GEO])

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
