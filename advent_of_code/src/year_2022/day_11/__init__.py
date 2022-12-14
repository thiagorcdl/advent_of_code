import re
from functools import lru_cache, reduce

from advent_of_code.src.utils import BaseSolution

PRIME_NUMBERS = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
    83, 89, 97
]


class Monkey:
    id: int
    items: list
    operation: str
    test_division: int
    test_division2: int
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

    @lru_cache(maxsize=None)
    def divisors(self):
        divisors = {self.test_division}
        divisor_queue = [self.test_division]
        for amount in range(1, 3):
            divisor_queue_copy = [x for x in divisor_queue]
            divisor_queue = []
            while divisor_queue_copy:
                existing_div = divisor_queue_copy.pop(0)
                for prime in PRIME_NUMBERS:
                    new_num = existing_div * prime
                    divisors.add(new_num)
                    divisor_queue.append(new_num)
        return sorted(list(divisors), reverse=True)


class Solution(BaseSolution):
    """Logics for solving day 11."""
    day = 11
    monkeys = []

    # example = True
    divisors = []
    divisor = 1
    divisor2 = 2
    divisor_count = 0

    def get_monkey_business(self):
        """Multiply two top inspection counts."""
        highest = [0, 0]
        for monkey in self.monkeys:
            for i in range(2):
                if monkey.inspection_count > highest[i]:
                    highest.insert(i, monkey.inspection_count)
                    highest.pop()
                    break

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
                divisor = int(match[0])
                curr_monkey.test_division = divisor
                curr_monkey.test_division2 = divisor * 2
                self.divisors.append(divisor)
            elif match := re.findall(r"If true: throw to monkey (\d+)", line):
                curr_monkey.destination_true = int(match[0])
            elif match := re.findall(r"If false: throw to monkey (\d+)", line):
                curr_monkey.destination_false = int(match[0])
                print(curr_monkey.divisors())

        self.divisor = reduce(lambda x, y: x * y, self.divisors)
        self.divisor2 = self.divisor * 2

    def simulate_round(self, part=1):
        """Simulate simian shenanigans for one round."""
        for monkey in self.monkeys:
            for old in monkey.items:
                new = eval(monkey.operation)

                if part == 1:
                    new = new // 3

                dest_monkey = monkey.destination_false
                dividend = new
                if dividend >= self.divisor2:
                    dividend = dividend % self.divisor
                if dividend == 0:
                    dest_monkey = monkey.destination_true
                else:
                    for divisor in monkey.divisors():
                        if divisor * 2 > dividend:
                            continue
                        dividend = dividend % divisor
                        if dividend == 0:
                            dest_monkey = monkey.destination_true
                            break

                self.monkeys[dest_monkey].items.append(new)

            monkey.inspection_count += len(monkey.items)
            monkey.items = []

    def part_1(self):
        """Find the level of monkey business after 20 rounds of stuff-slinging
        simian shenanigans.
        """
        self.setup()
        for r in range(20):
            print(f"ROUND {r} -------------------------------------------------")
            self.simulate_round()
        return self.get_monkey_business()

    def get_item_counts(self):
        return list(map(lambda x: len(x.items), self.monkeys))

    def get_inspec_counts(self):
        return [x.inspection_count for x in self.monkeys]

    def part_2(self):
        """Run solution for part 2."""
        self.setup()
        # prev = self.get_item_counts(), self.get_inspec_counts()
        print(self.divisor)
        n_rounds = 10000
        for r in range(1, n_rounds + 1):
            print(f"ROUND {r} -------------------------------------------------")
            self.simulate_round(part=2)
            print(self.get_inspec_counts())
        return self.get_monkey_business()  # 28500000000 < result < 28600000000
