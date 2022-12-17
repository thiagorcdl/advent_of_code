import re
import sys

from advent_of_code.src.utils import BaseSolution


class Node:

    def __init__(self, name, flow="0"):
        self.is_open = False
        self.open_time_left = None
        self.name = name
        self.flow = int(flow)
        self.neighbors = []

    def __repr__(self):
        if self.is_open:
            open_repr = f"OPEN : {self.flow} * {self.open_time_left}"
        else:
            open_repr = "----"
        return f"<{self.name} | {open_repr}>"


class Solution(BaseSolution):
    """Logics for solving day 16."""
    day = 16
    INIT_NODE = "AA"
    best_total = 0
    graph = dict()
    count = 0

    example = True

    def build_graph(self):
        for line in self.input_lines:
            name, flow = re.findall(f"Valve (\w+) has flow rate=(\d+);", line)[0]

            try:
                node = self.graph[name]
                node.flow = int(flow)
            except KeyError:
                node = Node(name, flow)
                self.graph[name] = node

            for neighbor_name in re.findall(f"valves? (.+)", line)[0].split(","):
                neighbor_name = neighbor_name.strip()
                try:
                    neighbor = self.graph[neighbor_name]
                except KeyError:
                    neighbor = Node(neighbor_name)
                    self.graph[neighbor_name] = neighbor
                node.neighbors.append(neighbor)

    def dfs(self, node, time=30, total=0):
        # print("-" * 80)
        # print(f"time left: {time}")
        # print(node)
        if time < 1:
            self.best_total = max(self.best_total, total)
            return
        self.count += 1
        if self.count > 1500000:
            sys.exit(1)

        # Open valve
        if not node.is_open:
            node.is_open = True
            new_time = time - 1
            node.open_time_left = new_time
            new_total = total + node.flow * time

            for neighbor in node.neighbors:
                self.dfs(neighbor, new_time - 1, new_total)

            node.is_open = False

        # Don't open
        for neighbor in node.neighbors:
            self.dfs(neighbor, time - 1, total)

    def part_1(self):
        """Run solution for part 1."""
        self.build_graph()
        for k, v in self.graph.items():
            print("="*80)
            print(k)
            print(v.name)
            print(v.flow)
        init_node = self.graph[self.INIT_NODE]
        for neighbor in init_node.neighbors:
            self.dfs(neighbor, 29, 0)
        return self.best_total

    def part_2(self):
        """Run solution for part 2."""
        total = 0
        for line in self.input_lines:
            pass
        return total
