import copy

from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 9."""
    day = 9

    def solve(self, part2=False):
        NCITIES = 8
        EXCLUDE = -1 if part2 else 2 ** 31
        cities = []
        graph = [[0 for x in range(NCITIES)] for y in range(NCITIES)]

        for line in self.input_lines:
            a, to, b, equals, distance = line.split(' ')
            if a not in cities:
                cities.append(a)
            if b not in cities:
                cities.append(b)
            graph[cities.index(a)][cities.index(b)] = int(distance)
            graph[cities.index(b)][cities.index(a)] = int(distance)

        totals = []
        for city in cities:
            graph2 = copy.deepcopy(graph)
            c = cities.index(city)
            visited = [c, ]
            total = 0
            trip = cities[c]
            while len(visited) < NCITIES:
                graph2[visited[-1]][visited[-1]] = EXCLUDE
                if len(visited) > 1:
                    graph2[visited[-1]][visited[-2]] = EXCLUDE
                options = graph2[visited[-1]]
                distance = max(*options) if part2 else min(*options)
                peer = options.index(distance)
                while peer in visited:
                    start = peer + 1
                    peer = options.index(distance, start)
                total += distance
                for i in range(NCITIES):
                    graph2[i][visited[-1]] = EXCLUDE
                visited.append(peer)
            totals.append(total)

        return max(totals) if part2 else min(totals)

    def part_1(self):
        """Run solution for part 1."""
        return self.solve()

    def part_2(self):
        """Run solution for part 2."""
        return self.solve(part2=True)
