from advent_of_code.src.constants import INFINITE
from advent_of_code.src.utils import BaseSolution

ELF = "#"
N_ROUNDS = 10

NORTH = "n"
SOUTH = "s"
WEST = "w"
EAST = "e"

DIR_LOOK_MODIFS = {
    NORTH: [(-1, -1), (-1, 0), (-1, 1)],
    SOUTH: [(1, -1), (1, 0), (1, 1)],
    WEST: [(-1, -1), (0, -1), (1, -1)],
    EAST: [(-1, 1), (0, 1), (1, 1)],
}
DIR_MOVE_MODIF = {
    NORTH: (-1, 0),
    SOUTH: (1, 0),
    WEST: (0, -1),
    EAST: (0, 1),
}


class Solution(BaseSolution):
    """Logics for solving day 23."""
    day = 23
    check_order = [NORTH, SOUTH, WEST, EAST]
    proposed_moves = dict()
    elves = dict()
    n_elves = 0
    stopped_elf_count = 0

    # example = True

    def read_map(self):
        """Get elves initial positions."""
        elf_id = 0
        for l, line in enumerate(self.input_lines):
            for c, val in enumerate(line):
                if val == ELF:
                    elf_id += 1
                    self.elves[(l, c)] = elf_id
        self.n_elves = len(self.elves)

    def propose_move(self, elf_pos):
        considered_moves = []
        for check_dir in self.check_order:
            pos_modifs = DIR_LOOK_MODIFS[check_dir]
            for modif_l, modif_c in pos_modifs:
                look_pos = elf_pos[0] + modif_l, elf_pos[1] + modif_c
                if look_pos in self.elves:
                    break
            else:
                # Nothing found in direction, propose move
                modif_l, modif_c = DIR_MOVE_MODIF[check_dir]
                next_pos = elf_pos[0] + modif_l, elf_pos[1] + modif_c
                considered_moves.append(next_pos)

        if 0 < len(considered_moves) < 4:
            # print(f"{self.elves[elf_pos]} {considered_moves}")
            next_pos = considered_moves[0]
            if next_pos in self.proposed_moves:
                # Someone already wants to go here, no one goes
                self.proposed_moves[next_pos] = None
            else:
                # Dibs!
                self.proposed_moves[next_pos] = elf_pos

    def move(self, next_pos, elf_pos):
        if elf_pos is None:
            return 0

        self.elves[next_pos] = self.elves.pop(elf_pos)
        return 1

    def simulate_round(self):
        self.proposed_moves = dict()
        move_count = 0
        for elf_pos in self.elves:
            self.propose_move(elf_pos)
        for next_pos, elf_pos in self.proposed_moves.items():
            move_count += self.move(next_pos, elf_pos)
        if move_count == 0:
            return False
        check_dir = self.check_order.pop(0)
        self.check_order.append(check_dir)
        return True

    def draw_map(self):
        low_l = low_c = INFINITE
        high_l = high_c = -9999
        for elf_l, elf_c in self.elves:
            low_l = min(low_l, elf_l)
            high_l = max(high_l, elf_l)
            low_c = min(low_c, elf_c)
            high_c = max(high_c, elf_c)

        for l in range(low_l, high_l + 1):
            line = ""
            for c in range(low_c, high_c + 1):
                line += ELF if (l, c) in self.elves else "."
            print(line)

    def calculate_spaced_ground(self):
        """Count empty cells in the rectangle that contains all elves."""
        low_l = low_c = INFINITE
        high_l = high_c = -9999
        for elf_l, elf_c in self.elves:
            low_l = min(low_l, elf_l)
            high_l = max(high_l, elf_l)
            low_c = min(low_c, elf_c)
            high_c = max(high_c, elf_c)

        height = high_l - low_l + 1
        length = high_c - low_c + 1
        return (height * length) - self.n_elves

    def part_1(self):
        """Run solution for part 1."""
        self.read_map()
        for i in range(N_ROUNDS):
            self.simulate_round()
        self.draw_map()
        return self.calculate_spaced_ground()

    def part_2(self):
        """Run solution for part 2."""
        self.read_map()
        i = 1
        while self.simulate_round():
            i += 1
        return i
