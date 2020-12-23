#!/usr/bin/env python
from src.utils import BaseResolution
import re

bag_map = dict()
part_1_bag_set = set()
part_2_child_count = dict()

class Bag:
    name: str
    parents: set
    children: set

    def __repr__(self):
        return f"<{self.name}>"

    def __init__(self, name, parent=None, children_name=None):
        self.name = name
        self.parents = {parent} if parent else set()

        self.children = set(children_name or [])

    def add_children(self, children_name):
        """Create new Bag objects and add to children."""
        if not children_name:
            part_2_child_count[self.name] = 0
            return
        for n, child_name in children_name:
            child = bag_map.setdefault(child_name, Bag(child_name))
            child.parents.add(self)
            self.children.add((int(n), child))

    def traverse_parents(self):
        """Recursively loop through parents."""
        part_1_bag_set.add(self.name)
        for parent in self.parents:
            parent.traverse_parents()

    def get_children_count(self):
        """Recursively loop through children to get their respective
        children amount.
        """
        part_2_child_count[self.name] = 0
        for n, child in self.children:
            grandchildren_count = part_2_child_count.setdefault(
                child.name, child.get_children_count()
            )
            part_2_child_count[self.name] += n * (grandchildren_count + 1)
        return part_2_child_count[self.name]


class Resolution(BaseResolution):
    """Logics for resolving day 7."""
    day = 7

    def part_1(self, input_lines: list):
        """Find how many bag colors can contain at least one shiny gold bag."""
        for line in input_lines:
            current_name, rest = line.split(" bags contain")
            match = re.findall(r" (\d+) ([ \w]+) bags?", rest)
            current = bag_map.setdefault(current_name, Bag(current_name))
            current.add_children(match)

        shiny_gold = bag_map["shiny gold"]
        shiny_gold.traverse_parents()
        print(len(part_1_bag_set) - 1)

    def part_2(self, input_lines: list):
        """Find how many individual bags are required inside your single shiny
        gold bag.
        """
        for line in input_lines:
            current_name, rest = line.split(" bags contain")
            match = re.findall(r" (\d+) ([ \w]+) bags?", rest)
            current = bag_map.setdefault(current_name, Bag(current_name))
            current.add_children(match)

        shiny_gold = bag_map["shiny gold"]
        shiny_gold.get_children_count()
        print(shiny_gold.get_children_count())

