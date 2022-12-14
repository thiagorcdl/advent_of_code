from json.encoder import INFINITY
from string import ascii_lowercase
from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 12."""
    START_MARKER = "S"
    END_MARKER = "E"
    day = 12
    start_pos: tuple
    start_pos_list = list()
    end_pos: tuple
    n_lines: int
    n_cols: int
    dir_map: list

    # example = True

    def parse_input(self):
        """Configure initial state."""

        self.n_lines = len(self.input_lines)
        self.n_cols = len(self.input_lines[0])
        self.dir_map = [
            [dict() for j in range(self.n_cols)]
            for i in range(self.n_lines)
        ]

        # Convert to numbers
        for l in range(self.n_lines):
            for c in range(self.n_cols):
                coords = l, c
                char = self.input_lines[l][c]

                if char == self.START_MARKER:
                    self.start_pos = coords
                    char = ascii_lowercase[0]
                elif char == self.END_MARKER:
                        self.end_pos = coords
                        char = ascii_lowercase[-1]

                if char == "a":
                    self.start_pos_list.append(coords)

                self.dir_map[l][c]["cost"] = INFINITY
                self.dir_map[l][c]["val"] = ascii_lowercase.index(char)
                self.dir_map[l][c]["edges"] = []

        # Find edges
        for l in range(self.n_lines):
            for c in range(self.n_cols):
                val = self.dir_map[l][c]["val"]

                # Check up
                if l > 0 and self.dir_map[l - 1][c]["val"] >= val - 1:
                    self.dir_map[l][c]["edges"].append((l - 1, c))

                # Check left
                if c > 0 and self.dir_map[l][c - 1]["val"] >= val - 1:
                    self.dir_map[l][c]["edges"].append((l, c - 1))

                # Check down
                if l < self.n_lines - 1 and self.dir_map[l + 1][c]["val"] >= val - 1:
                    self.dir_map[l][c]["edges"].append((l + 1, c))

                # Check right
                if c < self.n_cols - 1 and self.dir_map[l][c + 1]["val"] >= val - 1:
                    self.dir_map[l][c]["edges"].append((l, c + 1))

    def dijkstra(self, start_pos):
        unvisited = [
            (i, j)
            for j in range(self.n_cols)
            for i in range(self.n_lines)
        ]
        back_track = dict()
        back_track[str(start_pos)] = None
        self.dir_map[start_pos[0]][start_pos[1]]["cost"] = 0

        while unvisited:
            best_idx = 0
            for i in range(len(unvisited)):
                best_l, best_c = unvisited[best_idx]
                best = self.dir_map[best_l][best_c]
                new_l, new_c = unvisited[i]
                new = self.dir_map[new_l][new_c]

                if new["cost"] < best["cost"]:
                    best_idx = i

            curr_l, curr_c = unvisited.pop(best_idx)
            curr = self.dir_map[curr_l][curr_c]

            for neigh_l, neigh_c in curr["edges"]:
                neighbor = self.dir_map[neigh_l][neigh_c]
                curr_cost = curr["cost"] + 1

                if curr_cost < neighbor["cost"]:
                    neighbor["cost"] = curr_cost
                    back_track[str((neigh_l, neigh_c))] = curr_l, curr_c

        return back_track

    def part_1(self):
        """Find the fewest steps required to move from start_pos to end_pos."""
        self.parse_input()
        self.dijkstra(self.end_pos)
        return self.dir_map[self.start_pos[0]][self.start_pos[1]]["cost"]

    def part_2(self):
        """Find the fewest steps required to move from any 'a' to end_pos."""
        self.parse_input()
        self.dijkstra(self.end_pos)
        lowest = min([self.dir_map[l][c]["cost"] for l, c in self.start_pos_list])
        return lowest
