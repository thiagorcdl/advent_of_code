#!/usr/bin/env python
from advent_of_code.src.utils import BaseResolution


class Resolution(BaseResolution):
    """Logics for resolving day 3."""
    day = 3

    def count_bits(self, number_list: list) -> list:
        """Return list with the most common bit (str) for each bit index."""
        bitcount = []
        for line in number_list:
            for bit_idx, bit in enumerate(line):
                value = int(bit)
                try:
                    bitcount[bit_idx] += value
                except IndexError:
                    bitcount.append(value)
        return bitcount

    def build_common_mask(self, bitcount: list, length: int, invert=False) -> str:
        """Return bit sequence of the most common bit for each index."""
        common_bit = "0" if invert else "1"
        uncommon_bit = "1" if invert else "0"
        threshold = length / 2
        bits_str = ""
        for count in bitcount:
            bits_str += common_bit if count >= threshold else uncommon_bit
        return bits_str

    def build_rate(self, common_mask: str, invert=False) -> int:
        """Return base10 value, given the most common bits."""
        if invert:
            bits_str = ""
            for bit in common_mask:
                bits_str += "0" if bit == "1" else "1"
        else:
            bits_str = common_mask
        return int(bits_str, 2)

    def part_1(self):
        """Calculate the power consumption of the submarine, mulyipltying gama and
        epsilon rates.
        """
        bitcount = self.count_bits(self.input_lines)
        length = len(self.input_lines)
        common_mask = self.build_common_mask(bitcount, length)
        gamma = self.build_rate(common_mask)
        epsilon = self.build_rate(common_mask, invert=True)
        print(gamma * epsilon)

    def search_gas(self, number_list, invert=False):
        """Yield the number corresponding to the oxygen rating, considering most
        common bit.

        Invert common mask for CO2.
        """
        number_list_copy = [x for x in number_list]
        bit_idx = 0
        length = len(number_list_copy)

        while length > 1:
            bitcount = self.count_bits(number_list_copy)
            common_mask = self.build_common_mask(bitcount, length, invert=invert)

            number_list_copy = [
                number for number in number_list_copy
                if number[bit_idx] == common_mask[bit_idx]
            ]

            bit_idx += 1
            length = len(number_list_copy)

        return self.build_rate(number_list_copy[0])

    def part_2(self):
        """Return the life support rating of the submarine, multiplying oxygen and
        CO2 ratings.
        """
        number_list = [line.strip() for line in self.input_lines]
        oxygen = self.search_gas(number_list)
        carbon_dioxide = self.search_gas(number_list, invert=True)
        print(oxygen * carbon_dioxide)


