import re
from string import ascii_uppercase

from advent_of_code.src.utils import BaseSolution

EMPTY_LINE = ""
PATH = "."
BLK = "#"
VOID = " "

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

DIR_MODIFS = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0),
}

ROT_MODIF = {
    "R": 1,
    "L": -1,
}


class Solution(BaseSolution):
    """Logics for solving day 22."""
    day = 22
    board = []
    instructions = None
    facing = RIGHT
    pos = tuple()

    # example = True

    def read_input(self):
        """Build board and load instructions."""
        delim_idx = self.input_lines.index(EMPTY_LINE)
        highest_dim = 0
        for line in self.input_lines[:delim_idx]:
            new_line = VOID + line + VOID
            highest_dim = max(highest_dim, len(new_line))
            self.board.append(new_line)

        void_line = VOID * highest_dim
        self.pos = 1, self.board[0].index(PATH)
        for i in range(len(self.board)):
            line_len = len(self.board[i])
            if line_len < highest_dim:
                self.board[i] += VOID * (highest_dim - line_len)
        self.board.insert(0, void_line)
        self.board.append(void_line)
        self.instructions = self.input_lines[-1]
        self.instructions = re.findall(r"(\d+|\w)", self.input_lines[-1])

    def get_next_cell(self):
        """Calculate next pos and get value."""
        modif = DIR_MODIFS[self.facing]
        next_pos = [self.pos[i] + modif[i] for i in range(2)]
        next_val = self.board[next_pos[0]][next_pos[1]]
        if next_val != VOID:
            return next_pos, next_val

        # Find wrap-around
        if self.facing == RIGHT:
            i = 0
            max_len = len(self.board[next_pos[0]])
            while self.board[next_pos[0]][i] == VOID:
                i = (i + 1) % max_len
            next_pos = next_pos[0], i
        elif self.facing == DOWN:
            i = 0
            max_len = len(self.board)
            while self.board[i][next_pos[1]] == VOID:
                i = (i + 1) % max_len
            next_pos = i, next_pos[1]
        elif self.facing == LEFT:
            i = -1
            max_len = len(self.board[next_pos[0]])
            while self.board[next_pos[0]][i] == VOID:
                i = (i - 1) % max_len
            next_pos = next_pos[0], i
        elif self.facing == UP:
            i = -1
            max_len = len(self.board)
            while self.board[i][next_pos[1]] == VOID:
                i = (i - 1) % max_len
            next_pos = i, next_pos[1]
        next_val = self.board[next_pos[0]][next_pos[1]]
        return next_pos, next_val

    def follow_directions(self):
        """Simulate walking through the board."""
        while self.instructions:
            inst = self.instructions.pop(0)
            if inst in ascii_uppercase:
                self.facing = (self.facing + ROT_MODIF[inst]) % 4
                continue

            n_moves = int(inst)
            while n_moves:
                next_pos, next_val = self.get_next_cell()
                if next_val == PATH:
                    # Keep moving
                    self.pos = next_pos
                    n_moves -= 1
                    continue
                elif next_val == BLK:
                    # Hit wall, stop moving
                    break

    def calculate_result(self):
        return 1000 * self.pos[0] + 4 * self.pos[1] + self.facing

    def part_1(self):
        """Run solution for part 1."""
        self.read_input()
        self.follow_directions()
        return self.calculate_result()

    def part_2(self):
        """Run solution for part 2."""
        total = 0
        for line in self.input_lines:
            pass
        return total
