from advent_of_code.src.utils import BaseSolution

BLK = "#"
_s_ = " "


class RockBase:
    pattern: list
    line: int
    col: int

    left_modifs = []
    right_modifs = []
    down_modifs = []

    def __init__(self, map_top):
        self.line = map_top + 3 + self.height
        self.col = 2

    @property
    def pos(self):
        return self.line, self.col

    @property
    def height(self):
        return len(self.pattern)

    def left_perim(self):
        return [
            (self.line + modif_l, self.col + modif_c)
            for modif_l, modif_c in self.left_modifs
        ]

    def right_perim(self):
        return [
            (self.line + modif_l, self.col + modif_c)
            for modif_l, modif_c in self.right_modifs
        ]

    def down_perim(self):
        return [
            (self.line + modif_l, self.col + modif_c)
            for modif_l, modif_c in self.down_modifs
        ]

    def settle(self, map):
        for l, line in enumerate(self.pattern):
            for c, item in enumerate(line):
                if item == BLK:
                    map[self.col + c][self.line - l] = BLK
        return map


class HorizonRock(RockBase):
    pattern = [
        [BLK, BLK, BLK, BLK]
    ]
    left_modifs = [(0, -1)]
    right_modifs = [(0, 4)]
    down_modifs = [(-1, 0), (-1, 1), (-1, 2), (-1, 3)]


class CrossRock(RockBase):
    pattern = [
        [_s_, BLK, _s_],
        [BLK, BLK, BLK],
        [_s_, BLK, _s_]
    ]
    left_modifs = [(0, 0), (-1, -1), (-2, 0)]
    right_modifs = [(0, 2), (-1, 3), (-2, 2)]
    down_modifs = [(-2, 0), (-3, 1), (-2, 2)]


class ElleRock(RockBase):
    pattern = [
        [_s_, _s_, BLK],
        [_s_, _s_, BLK],
        [BLK, BLK, BLK],
    ]
    left_modifs = [(0, 1), (-1, 1), (-2, -1)]
    right_modifs = [(0, 3), (-1, 3), (-2, 3)]
    down_modifs = [(-3, 0), (-3, 1), (-3, 2)]


class VerticalRock(RockBase):
    pattern = [
        [BLK],
        [BLK],
        [BLK],
        [BLK],
    ]
    left_modifs = [(0, -1), (-1, -1), (-2, -1), (-3, -1)]
    right_modifs = [(0, 1), (-1, 1), (-2, 1), (-3, 1)]
    down_modifs = [(-4, 0)]


class SquareRock(RockBase):
    pattern = [
        [BLK, BLK],
        [BLK, BLK]
    ]

    left_modifs = [(0, -1), (-1, -1)]
    right_modifs = [(0, 2), (-1, 2)]
    down_modifs = [(-2, 0), (-2, 1)]


class Solution(BaseSolution):
    """Logics for solving day 17."""
    WIDTH = 7
    ROCK_LIMIT1 = 2022
    ROCK_LIMIT2 = 1000000000000
    ROCK_ORDER = [HorizonRock, CrossRock, ElleRock, VerticalRock, SquareRock]
    CLASS_COUNT = len(ROCK_ORDER)
    top = -1
    map = [{-1: BLK} for _ in range(WIDTH)]  # map[COL][LIN]
    jet_order = []
    jet_count = 0
    step = 0
    day = 17
    cycle = []

    # example = True

    def increase_step(self):
        # Next step
        if self.step == self.jet_count - 1:
            # Keeping int low to save time on mod
            self.step = 0
        else:
            self.step += 1

    def rockfall(self, rock_count):
        """Simulate rock falling and hitting obstacles."""
        rock_class = self.ROCK_ORDER[rock_count % self.CLASS_COUNT]
        rock = rock_class(self.top)

        while True:
            # Jet
            jet = self.jet_order[self.step]
            self.increase_step()

            if jet == "<":
                # Left
                free = True
                for l, c in rock.left_perim():
                    try:
                        if c < 0 or self.map[c][l] == BLK:
                            free = False
                    except KeyError:
                        # If nothing mapped, then it's free
                        pass
                if free:
                    rock.col -= 1
            elif jet == ">":
                # Right
                free = True
                for l, c in rock.right_perim():
                    try:
                        if c >= self.WIDTH or self.map[c][l] == BLK:
                            free = False
                    except KeyError:
                        # If nothing mapped, then it's free
                        pass
                if free:
                    # Move piece right
                    rock.col += 1
            else:
                print("jet")

            # Fall down
            free = True
            for l, c in rock.down_perim():
                try:
                    if self.map[c][l] == BLK:
                        free = False
                except KeyError:
                    # If nothing mapped, then it's free
                    pass
            if free:
                # Move piece down
                rock.line -= 1
            else:
                self.top = max(self.top, rock.line)
                self.map = rock.settle(self.map)
                break

    def part_1(self):
        """Run solution for part 1."""
        self.jet_order = self.input_lines[0]
        self.jet_count = len(self.jet_order)
        for rock_count in range(self.ROCK_LIMIT1):
            self.rockfall(rock_count)
        return self.top + 1

    def find_period(self):
        """Check if current line has happeneed before.
        Then check if previous line equals previous of the match.
        """

        def get_line(i):
            line = ""
            for col in self.map:
                try:
                    line += col[i]
                except KeyError:
                    line += _s_
            return line

        if self.top < 40:
            return None, None

        i = self.top
        curr_line = get_line(i)

        for j in range(i - 20, self.top // 2 - 20, -1):
            match_line = get_line(j)
            if match_line != curr_line:
                continue

            dist = i - j
            is_match = True
            for k in range(j - 1, j - dist, -1):
                if get_line(k) != get_line(k + dist):
                    is_match = False
                    break
            if is_match:
                return k, dist
        return None, None

    def part_2(self):
        """Run solution for part 2."""
        rock_limit = self.ROCK_LIMIT2
        total = 1
        self.jet_order = self.input_lines[0]
        self.jet_count = len(self.jet_order)

        cycle_start = None
        cycle_end = None
        last_period_height = 0
        top_first_cycle = 0

        for rock_count in range(rock_limit):
            self.rockfall(rock_count)
            period_start, period_height = self.find_period()
            if period_height:
                if not cycle_start:
                    cycle_start = rock_count
                    last_period_height = period_height
                    top_first_cycle = self.top
                elif period_height == last_period_height == (
                    self.top - top_first_cycle):
                    cycle_end = rock_count
                    break

        period_len = cycle_end - cycle_start
        rest_limit = (rock_limit - rock_count)
        period_count = rest_limit // period_len - 2
        periodicable_top = period_height * period_count
        total += periodicable_top
        REST_MAGIC_NUMBER = 0 if self.example else 1
        rest = rest_limit - period_count * period_len - REST_MAGIC_NUMBER

        # Simulate for rest
        for rock_count2 in range(rest):
            self.rockfall(rock_count2 + rock_count)
        total += self.top
        return total
