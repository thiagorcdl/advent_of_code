from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 2."""
    day = 2

    LOSS = 0
    DRAW = 3
    WIN = 6

    def part_1(self):
        """Return the total score considering th esecond column says which shape to
        play.
        """
        SHAPE_POINTS_MAP = {
            "X": 1,
            "Y": 2,
            "Z": 3,
        }
        RESULT_MAP = {
            "A": {
                "X": self.DRAW,  # ROCK / ROCK
                "Y": self.WIN,  # ROCK / PAPER
                "Z": self.LOSS,  # ROCK / SCISSOR
            },
            "B": {
                "X": self.LOSS,  # PAPER / ROCK
                "Y": self.DRAW,  # PAPER / PAPER
                "Z": self.WIN,  # PAPER / SCISSOR
            },
            "C": {
                "X": self.WIN,  # SCISSOR / ROCK
                "Y": self.LOSS,  # SCISSOR / PAPER
                "Z": self.DRAW,  # SCISSOR / SCISSOR
            },
        }

        total = 0
        for line in self.input_lines:
            enemy_shape, my_shape = line.split()
            shape_points = SHAPE_POINTS_MAP[my_shape]
            result_points = RESULT_MAP[enemy_shape][my_shape]
            total += shape_points + result_points
        return total

    def part_2(self):
        """Return total score considering the second column says the desired result
        of the match.
        """
        SHAPE_POINTS_MAP = {
            "A": 1,
            "B": 2,
            "C": 3,
        }
        RESULT_MAP = {
            "A": {
                "X": (self.LOSS, "C"),  # ROCK / SCISSOR
                "Y": (self.DRAW, "A"),  # ROCK / ROCK
                "Z": (self.WIN, "B"),  # ROCK / PAPER
            },
            "B": {
                "X": (self.LOSS, "A"),  # PAPER / ROCK
                "Y": (self.DRAW, "B"),  # PAPER / PAPER
                "Z": (self.WIN, "C"),  # PAPER / SCISSOR
            },
            "C": {
                "X": (self.LOSS, "B"),  # SCISSOR / PAPER
                "Y": (self.DRAW, "C"),  # SCISSOR / SCISSOR
                "Z": (self.WIN, "A"),  # SCISSOR / ROCK
            },
        }

        total = 0
        for line in self.input_lines:
            enemy_shape, result = line.split()
            result_points, my_shape = RESULT_MAP[enemy_shape][result]
            shape_points = SHAPE_POINTS_MAP[my_shape]
            total += shape_points + result_points
        return total
