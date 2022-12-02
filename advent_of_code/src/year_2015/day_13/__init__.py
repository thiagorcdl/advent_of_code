import itertools

from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 13."""
    day = 13

    def solve(self, part2=False):
        NPEOPLE = 9 if part2 else 8
        EXCLUDE = 2 ** 31 if part2 else -(2 ** 31)
        people = []
        graph = [[0 for x in range(NPEOPLE)] for y in range(NPEOPLE)]

        # Build Graph
        for line in self.input_lines:
            split = line.replace('lose ', '-').replace('gain ', '').split(' ')
            a, value, b = split[0], split[2], split[-1][:-1]
            if a not in people:
                people.append(a)
            if b not in people:
                people.append(b)
            graph[people.index(a)][people.index(b)] += int(value)
            graph[people.index(b)][people.index(a)] += int(value)

        # Include yourself in part 2
        if part2:
            for i in range(NPEOPLE):
                graph[i][NPEOPLE - 1] = 0

        # Held-Karp algorithm
        peopleset = set(range(NPEOPLE))
        costs = [{} for x in range(NPEOPLE)]

        for k in range(1, NPEOPLE):
            costs[k]['{0, %d}' % k] = graph[0][k]

        for i in range(2, NPEOPLE + 1):
            for subset in sorted(itertools.combinations(peopleset, i),
                                 key=lambda tup: tup[0]):
                for k in reversed(subset):
                    try:
                        costs[k][repr(set(subset))] = max(
                            [costs[j][repr(set(subset).difference({k}))] + graph[j][k]
                             for j in subset if j not in [0, k]]
                        )
                    except:
                        pass
        return max(
            [costs[k][repr(peopleset)] + graph[k][0] for k in range(1, NPEOPLE)])

    def part_1(self):
        """Run solution for part 1."""
        return self.solve()

    def part_2(self):
        """Run solution for part 2."""
        return self.solve(part2=True)


