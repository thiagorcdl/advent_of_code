from advent_of_code.src.utils import BaseSolution


class Solution(BaseSolution):
    """Logics for solving day 8."""
    day = 7
    var = {}

    def AND(self, a, b):
        return self.get_val(a) & self.get_val(b)

    def OR(self, a, b):
        return self.get_val(a) | self.get_val(b)

    def LSHIFT(self, a, n):
        return self.get_val(a) * (2 ** int(n))

    def RSHIFT(self, a, n):
        return self.get_val(a) // (2 ** int(n))

    def get_val(self, key):
        try:
            return int(key)
        except:
            args = self.var[key]
            if isinstance(args, type(1)):
                return args
            elif len(args) == 1:  # 4000 -> a
                self.var[key] = 0x0000ffff & self.get_val(args[0])
            elif len(args) == 2:  # NOT a -> b
                self.var[key] = 0x0000ffff & ~ self.get_val(args[1])
            else:  # a OP n -> c
                self.var[key] = 0x0000ffff & eval("self.%s(args[0],args[2])" % args[1])
        return self.var[key]

    def part_1(self):
        """Run solution for part 1."""
        for line in self.input_lines:
            args = line.split(' ')
            self.var[args[-1]] = args[:-2]

        return 0x0000ffff & self.get_val('a')

    def part_2(self):
        """Run solution for part 2."""
        for line in self.input_lines:
            self.var[args[-1]] = args[:-2]

        var2 = var.copy()
        val_a = self.get_val('a')
        var = var2
        self.var['b'] = val_a

        return 0x0000ffff & self.get_val('a')


