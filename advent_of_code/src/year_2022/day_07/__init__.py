import re

from advent_of_code.src.constants import INFINITE
from advent_of_code.src.utils import BaseSolution


class Directory:
    name = ""
    size = 0
    files = dict()
    directories = dict()
    parent = None

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.size = 0
        self.files = dict()
        self.directories = dict()

    def get_total_size(self):
        """Recursively get size of directories."""
        total = self.size
        for directory in self.directories.values():
            total += directory.get_total_size()


class Solution(BaseSolution):
    """Logics for solving day 7."""
    MAX_SIZE = 100000
    DISK_SPACE = 70000000
    REQUIRED_SPACE = 30000000
    day = 7
    total = 0
    root = None
    sizes = []

    def get_total_size(self, curr_dir: Directory):
        """Recursively get size of directories."""
        for sub_dir in curr_dir.directories.values():
            curr_dir.size += self.get_total_size(sub_dir)

        if curr_dir.size <= self.MAX_SIZE:
            self.total += curr_dir.size

        self.sizes.append(curr_dir.size)
        return curr_dir.size

    def build_filesystem(self):
        """Consume commands to create directory tree."""
        self.root = curr_dir = None
        for line in self.input_lines:
            if line == "$ cd ..":
                # Go back
                curr_dir = curr_dir.parent
            elif match := re.match(r"\$ cd (.*)", line):
                # Change directory
                dir_name = match.groups()[0]
                try:
                    curr_dir = curr_dir.directories[dir_name]
                except AttributeError:
                    # Root - only first time
                    self.root = curr_dir = Directory(dir_name, parent=curr_dir)
            elif match := re.match(r"dir (.*)", line):
                # Listed directory
                dir_name = match.groups()[0]
                sub_dir = Directory(dir_name, parent=curr_dir)
                curr_dir.directories[dir_name] = sub_dir
            elif match := re.match(r"(\d+) (.*)", line):
                # Listed directory
                file_size = int(match.groups()[0])
                file_name = match.groups()[1]
                curr_dir.files[file_name] = file_size
                curr_dir.size += file_size

    def part_1(self):
        """Find the sum of sizes of directories with size <= MAX_SIZE."""
        self.build_filesystem()
        self.get_total_size(self.root)
        return self.total

    def part_2(self):
        """Find single directory with size >= needed free space."""
        self.build_filesystem()
        self.get_total_size(self.root)
        free_space = self.DISK_SPACE - self.root.size
        space_to_free = self.REQUIRED_SPACE - free_space

        lowest = INFINITE
        for size in self.sizes:
            if space_to_free <= size < lowest:
                lowest = size
        return lowest
