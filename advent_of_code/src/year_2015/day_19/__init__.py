import re

from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 19."""
    day = 19

    def solve(self, part2=False):
        mol = re.findall(r'\n\n(\w+)', self.raw_input)[0]
        outcomes = []

        if part2:
            path = []
            transit = {}

            def dissolve(mol):
                best = 2 ** 32
                if mol == 'e':
                    return len(path)
                if len(path) >= best - 1:
                    # After next transition, it will be just as good as current best
                    return best
                for key, val in transit.items():
                    for match in re.finditer(key, mol):
                        mol = mol[:match.start()] + val + mol[match.end():]
                        path.append(val)
                        best = min(best, dissolve(mol))
                        del path[-1]
                        mol = mol[:match.start()] + key + mol[
                                                          match.start() + len(val):]
                return best

            for key, val in re.findall(r'(\w+) => (\w+)', self.raw_input):
                transit[val] = key
            return dissolve(mol)
        else:
            for key, val in re.findall(r'(\w+) => (\w+)', self.raw_input):
                for match in re.finditer(key, mol):
                    outcomes.append(mol[:match.start()] + val + mol[match.end():])
            return len(set(outcomes))

    def part_1(self):
        """Run solution for part 1."""
        return self.solve()

    def part_2(self):
        """Run solution for part 2."""
        return self.solve(part2=True)
