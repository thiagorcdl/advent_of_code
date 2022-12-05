import re

from advent_of_code.src.constants import INFINITE
from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 19."""
    day = 19

    mutation_map = dict()
    PRIME_MOLECULE = 'e'
    lowest_path = INFINITE

    def part_1(self):
        """Find how many distinct molecules can be created."""
        mol = re.findall(r'\n\n(\w+)', self.raw_input)[0]
        outcomes = []
        for key, val in re.findall(r'(\w+) => (\w+)', self.raw_input):
            for match in re.finditer(key, mol):
                outcomes.append(mol[:match.start()] + val + mol[match.end():])
        return len(set(outcomes))

    def dissolve_molecule(self, molecule, n_steps=0):
        """Recursively swap molecules by its a source-molecule to return number of
        steps until PRIME_MOLECULE is found.
        """
        if molecule == self.PRIME_MOLECULE:
            self.lowest_path = min(self.lowest_path, n_steps)
            return
        if n_steps >= self.lowest_path - 1:
            return

        for mutated, dissolved in self.mutation_map.items():
            for match in re.finditer(mutated, molecule):
                new_molecule = (
                    molecule[:match.start()] + dissolved + molecule[match.end():]
                )
                self.dissolve_molecule(new_molecule, n_steps + 1)
        return

    def part_2(self):
        """Find the fewest number of steps to go from e to the medicine molecule."""
        for source, mutated in re.findall(r'(\w+) => (\w+)', self.raw_input):
            self.mutation_map[mutated] = source

        medicine = self.input_lines[-1]
        self.dissolve_molecule(medicine)
        return self.lowest_path
