import re

from advent_of_code.src.utils import BaseSolution


class Monkey:
    id: int
    items: list
    operation: str
    test_division: int
    destination_true: int
    destination_false: int
    inspection_count: int

    def __init__(self, monkey_id=0):
        self.inspection_count = 0
        self.id = monkey_id

    def __repr__(self):
        item_str = ", ".join([str(x) for x in self.items])
        text = f"Monkey {self.id}\n"
        text += f"  Starting items: {item_str}\n"
        text += f"  Operation: new = {self.operation}\n"
        text += f"  Test: divisible by {self.test_division}\n"
        text += f"    If true: throw to monkey {self.destination_true}\n"
        text += f"    If false: throw to monkey {self.destination_false}\n\n"
        return text


class Solution(BaseSolution):
    """Logics for solving day 11."""
    day = 11
    monkeys = []

    # example = True

    def get_monkey_business(self):
        """Multiply two top inspection counts."""
        highest = [0, 0]
        for monkey in self.monkeys:
            for i in range(2):
                if monkey.inspection_count > highest[i]:
                    highest.insert(i, monkey.inspection_count)
                    highest.pop()
                    break

        print(highest)
        return highest[0] * highest[1]

    def setup(self):
        """Read input and set initial values for simulation."""
        curr_monkey = None

        for line in self.input_lines:
            if "Monkey" in line:
                curr_monkey = Monkey(len(self.monkeys))
                self.monkeys.append(curr_monkey)
            elif match := re.findall(r"Starting items: (.+)", line):
                items = [int(x) for x in match[0].split(",")]
                curr_monkey.items = items
            elif match := re.findall(r"Operation: new = (.+)", line):
                curr_monkey.operation = match[0]
            elif match := re.findall(r"Test: divisible by (\d+)", line):
                curr_monkey.test_division = int(match[0])
            elif match := re.findall(r"If true: throw to monkey (\d+)", line):
                curr_monkey.destination_true = int(match[0])
            elif match := re.findall(r"If false: throw to monkey (\d+)", line):
                curr_monkey.destination_false = int(match[0])
                print(curr_monkey)

    def simulate_turn(self):
        """Simulate simian shenanigans for one round."""
        for monkey in self.monkeys:
            print(f"Monkey {monkey.id}")
            for old in monkey.items:
                print(f"\tInspects item {old}")
                increased = eval(monkey.operation)
                print(f"\t\tWorry increased to {increased}")
                decreased = increased // 3
                print(f"\t\tWorry decreased to {decreased}")

                if decreased % monkey.test_division == 0:
                    print(f"\t\tIs divisible by {monkey.test_division}")
                else:
                    print(f"\t\tIs NOT divisible by {monkey.test_division}")

                dest_monkey = (
                    monkey.destination_true
                    if (decreased % monkey.test_division) == 0
                    else monkey.destination_false
                )
                print(f"\t\tItem {decreased} is thrown to {dest_monkey}")
                self.monkeys[dest_monkey].items.append(decreased)

            monkey.inspection_count += len(monkey.items)
            monkey.items = []
            print(f"\t Inspection count: {monkey.inspection_count}\n")

    def part_1(self):
        """Find the level of monkey business after 20 rounds of stuff-slinging
        simian shenanigans.
        """
        self.setup()
        for turn in range(20):
            print(f"TURN {turn} -------------------------------------------------")
            self.simulate_turn()
        return self.get_monkey_business()

    def part_2(self):
        """Run solution for part 2."""
        total = 0
        for line in self.input_lines:
            pass
        return total
