#!/usr/bin/env python
from advent_of_code.src.utils import BaseResolution

GRID_SIZE = 5


class Board:
    """Representation of a bingo board."""

    id = None
    current_round = -1
    grid = None # 5x5
    round_won = None
    winning_number = None

    def __init__(self, board_id, input_grid):
        """Initialize board with given grid of numbers."""
        self.id = board_id
        self.grid = []

        for row in range(GRID_SIZE):
            self.grid.append([])
            input_line = input_grid[row].strip().split()
            for col in range(GRID_SIZE):
                self.grid[row].append({
                    "value": int(input_line[col]),
                    "marked": False,
                })

    def is_vertical_win(self, coords) -> bool:
        """Define whether current coords belong to a winning column."""
        col = coords[1]
        for row in range(GRID_SIZE):
            if not self.grid[row][col]["marked"]:
                return False

        return True

    def is_horizontal_win(self, coords) -> bool:
        """Define whether current coords belong to a winning row."""
        row = coords[0]
        for col in range(GRID_SIZE):
            if not self.grid[row][col]["marked"]:
                return False

        return True

    def find_number(self, number) -> tuple:
        """Return coords for given number, if present."""
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if number == self.grid[row][col]["value"]:
                    self.grid[row][col]["marked"] = True
                    return row, col

        return tuple()

    def draw_number(self, number):
        """Mark drawn number if it exists and check for board victory."""
        self.current_round += 1
        coords = self.find_number(number)
        if not coords:
            return

        won = self.is_vertical_win(coords) or self.is_horizontal_win(coords)
        if won:
            self.round_won = self.current_round
            self.winning_number = number

    @property
    def score(self):
        """Calculate the score multiplying winning_number by the sum of
        unmarked numbers.
        """
        unmarked_sum = 0
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if not self.grid[row][col]["marked"]:
                    unmarked_sum += self.grid[row][col]["value"]

        return self.winning_number * unmarked_sum


class Resolution(BaseResolution):
    """Logics for resolving day 4."""
    day = 4

    def part_1(self):
        """Find first board to win and print its score."""
        draws = list(map(int, self.input_lines[0].strip().split(",")))
        line_idx = 2
        board_idx = 0
        max_line = len(self.input_lines[line_idx:])

        earliest = None
        while line_idx < max_line:
            line = self.input_lines[line_idx].strip()
            if not line:
                # Empty line
                line_idx += 1
                continue

            # Read grid and build board
            previous_line_idx = line_idx
            line_idx += 5
            grid = self.input_lines[previous_line_idx: line_idx + 5]
            board = Board(board_idx, grid)
            for number in draws:
                board.draw_number(number)
                if board.round_won:
                    earliest = board
                    break
                elif earliest and board.current_round == earliest.round_won - 1:
                    break
            board_idx += 1

        return earliest.score

    def part_2(self):
        """Find last board to win and print its score."""
        draws = list(map(int, self.input_lines[0].strip().split(",")))
        line_idx = 2
        board_idx = 0
        max_line = len(self.input_lines[line_idx:])

        earliest = None
        while line_idx < max_line:
            line = self.input_lines[line_idx].strip()
            if not line:
                # Empty line
                line_idx += 1
                continue

            # Read grid and build board
            previous_line_idx = line_idx
            line_idx += 5
            grid = self.input_lines[previous_line_idx: line_idx + 5]
            board = Board(board_idx, grid)
            for number in draws:
                board.draw_number(number)
                if not board.round_won:
                    continue
                if not earliest or board.round_won > earliest.round_won:
                    earliest = board
                break
            board_idx += 1

        return earliest.score


