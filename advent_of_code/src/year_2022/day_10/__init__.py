from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 10."""
    INITIAL_REGISTER = 1
    CYCLE_CHECKPOINTS = [20, 60, 100, 140, 180, 220]
    CYCLE_MAP = {
        "noop": 1,
        "addx": 2,
    }
    day = 10
    checkpoint = 0
    total = 0
    cycle = 0
    register = INITIAL_REGISTER
    screen = []

    def set_signal_strength(self):
        """Increase cycle value and increase total."""
        self.cycle += 1
        if self.cycle == self.CYCLE_CHECKPOINTS[self.checkpoint]:
            self.total += self.cycle * self.register
            self.checkpoint += 1

        if self.checkpoint >= len(self.CYCLE_CHECKPOINTS):
            return True
        return False

    def part_1(self):
        """Find the sum of signal strengths during the 20th, 60th, 100th, 140th,
        180th, and 220th cycles.
        """
        for line in self.input_lines:
            x_val = line.split()[-1]
            if self.set_signal_strength():
                break

            if x_val != "noop":
                if self.set_signal_strength():
                    break
                self.register += int(x_val)
        return self.total

    def draw_pixels(self):
        """Increase cycle value and SET CRT image."""
        self.cycle += 1
        crt = self.cycle % 40 - 1
        char = "#" if abs(self.register - crt) < 2 else " "
        self.screen.append(char)

    def part_2(self):
        """Run solution for part 2."""
        for line in self.input_lines:
            x_val = line.split()[-1]
            self.draw_pixels()

            if x_val != "noop":
                self.draw_pixels()
                self.register += int(x_val)

        for i in range(6):
            line = "".join(self.screen[40*i:40*(i+1)])
            print(line)
        return ""


