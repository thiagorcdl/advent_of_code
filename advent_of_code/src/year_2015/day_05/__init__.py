from advent_of_code.src.utils import BaseResolution


class Resolution(BaseResolution):
    """Logics for resolving day 5."""
    day = 5

    def part_2(self):
        """Run solution for part 2."""
        total = 0

        for line in self.input_lines:
            tem_par, tem_amigo = False, False

            for i in range(len(line)-2):
                par = line[i:i+2]
                resto = line[i+2:]
                if par[0] == resto[0]:
                    tem_amigo = True
                if len(resto) > 1:
                    for j in range(len(resto)):
                        par2 = resto[j:j+2]
                        if par == par2:
                            tem_par = True
                            break
                if tem_par and tem_amigo:
                    total += 1
                    break

        return total
