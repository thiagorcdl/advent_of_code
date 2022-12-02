from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 14."""
    day = 14

    def solve(self, part2=False):
        finish = 2503

        total = 0
        timeline = [[] for s in range(finish)]
        stars = []

        def distance(speed, traveltime, resttime, finish=finish):
            time_sum = traveltime + resttime
            return finish // time_sum * speed * traveltime + min(finish % time_sum,
                                                                traveltime) * speed

        for line in self.input_lines:
            args = line.split(' ')
            name, speed, traveltime, resttime = args[0], int(args[3]), int(
                args[6]), int(args[-2])
            if part2:
                for t in range(1, finish + 1):
                    timeline[t - 1].append(distance(speed, traveltime, resttime, t))
                stars.append(0)
            else:
                total = max(total, distance(speed, traveltime, resttime))

        if part2:
            d3 = lambda x: '%4d' % x
            for t in range(finish):
                stars[timeline[t].index(max(timeline[t]))] += 1
            return max(stars)
        else:
            return total

    def part_1(self):
        """Run solution for part 1."""
        return self.solve()

    def part_2(self):
        """Run solution for part 2."""
        return self.solve(part2=True)
