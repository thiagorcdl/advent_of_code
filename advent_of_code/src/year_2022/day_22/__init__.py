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

EDGES = {
    "A1": [(0, 50), (0, 99)],
    "A2": [(150, 0), (199, 0)],
    "B1": [(0, 50), (49, 50)],
    "B2": [(100, 0), (149, 0)],
    "C1": [(0, 100), (0, 149)],
    "C2": [(199, 0), (199, 49)],
    "D1": [(0, 149), (49, 149)],
    "D2": [(100, 99), (149, 99)],
    "E1": [(49, 100), (49, 149)],
    "E2": [(50, 99), (99, 99)],
    "F1": [(50, 50), (99, 50)],
    "F2": [(100, 0), (100, 49)],
    "G1": [(149, 50), (149, 99)],
    "G2": [(150, 49), (199, 49)],
}
for k, v in EDGES.items():
    EDGES[k] = [(x[0] + 1, x[1] + 1) for x in v]

HORIZONTAL = 0
VERTICAL = 1

EDGE_ORIENTATION = {
    "A1": HORIZONTAL,
    "A2": VERTICAL,
    "B1": VERTICAL,
    "B2": VERTICAL,
    "C1": HORIZONTAL,
    "C2": HORIZONTAL,
    "D1": VERTICAL,
    "D2": VERTICAL,
    "E1": HORIZONTAL,
    "E2": VERTICAL,
    "F1": VERTICAL,
    "F2": HORIZONTAL,
    "G1": HORIZONTAL,
    "G2": VERTICAL,
}

JUMP_MAP = {
    "A1": ("A2", RIGHT),
    "A2": ("A1", DOWN),
    "B1": ("B2", RIGHT),
    "B2": ("B1", RIGHT),
    "C1": ("C2", UP),
    "C2": ("C1", DOWN),
    "D1": ("D2", LEFT),
    "D2": ("D1", LEFT),
    "E1": ("E2", LEFT),
    "E2": ("E1", UP),
    "F1": ("F2", DOWN),
    "F2": ("F1", RIGHT),
    "G1": ("G2", LEFT),
    "G2": ("G1", UP),
}

JUMPS_DIRS = {
    RIGHT: ["D1", "E2", "D2", "G2"],
    DOWN: ["E1", "G1", "C2"],
    LEFT: ["B1", "F1", "B2", "A2"],
    UP: ["A1", "C1", "F2"],
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

    def follow_directions(self, part2=False):
        """Simulate walking through the board."""
        while self.instructions:
            inst = self.instructions.pop(0)
            if inst in ascii_uppercase:
                self.facing = (self.facing + ROT_MODIF[inst]) % 4
                continue

            n_moves = int(inst)
            while n_moves:
                next_pos, next_val = (
                    self.get_next_cell_cube() if part2 else self.get_next_cell()
                )
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

    def get_edge_list(self, edge_id):
        edge_start, edge_end = EDGES[edge_id]
        start_l, start_c = edge_start
        end_l, end_c = edge_end
        orientation = EDGE_ORIENTATION[edge_id]
        if orientation == HORIZONTAL:
            # Fixed line, variable column
            return [x for x in range(start_c, end_c+1)]
        else:
            # Fixed column, variable line
            return [x for x in range(start_l, end_l+1)]

    def get_next_cell_cube(self):
        """Calculate next pos and get value around the cube."""
        modif = DIR_MODIFS[self.facing]
        next_pos = [self.pos[i] + modif[i] for i in range(2)]
        next_val = self.board[next_pos[0]][next_pos[1]]
        if next_val != VOID:
            return next_pos, next_val

        for edge_id in JUMPS_DIRS[self.facing]:
            edge_start, edge_end = EDGES[edge_id]
            start_l, start_c = edge_start
            end_l, end_c = edge_end
            if not (start_l <= self.pos[0] <= end_l and start_c <= self.pos[1] <= end_c):
                continue

            # Make jump
            next_edge_id, next_facing = JUMP_MAP[edge_id]
            # print(f"Jumping from {edge_id} to {next_edge_id}")
            next_edge_start, next_edge_end = EDGES[next_edge_id]
            next_start_l, next_start_c = next_edge_start
            curr_edge_list = self.get_edge_list(edge_id)

            if EDGE_ORIENTATION[edge_id] == HORIZONTAL:
                idx_in_edge = curr_edge_list.index(self.pos[1])
            else:
                idx_in_edge = curr_edge_list.index(self.pos[0])

            if EDGE_ORIENTATION[next_edge_id] == HORIZONTAL:
                # Map vertical to horizontal
                next_pos = next_start_l, next_start_c + idx_in_edge
            else:
                # Same orientation, same coord mapping
                next_pos = next_start_l + idx_in_edge, next_start_c

            self.facing = next_facing
            break

        next_val = self.board[next_pos[0]][next_pos[1]]
        return next_pos, next_val

    def part_2(self):
        """Run solution for part 2."""
        self.read_input()
        self.follow_directions(part2=True)
        return self.calculate_result()  # 140214 < ANSWER
