"""Day 9 solution."""
import re
from functools import reduce

from helpers import read_input, timeit


@timeit
def part_1(lines: list[str]) -> int:
    """Solution to part 1."""
    solution = 0
    for line in lines:
        numbers = list(map(int, re.findall(r'-?\d+', line)))
        while any(numbers):
            solution += numbers[-1]
            numbers = [second - first for first, second in zip(numbers, numbers[1:])]
    return solution


@timeit
def part_2(lines: list[str]) -> int:
    """Solution to part 2."""
    solution = 0
    for line in lines:
        numbers = list(map(int, re.findall(r'-?\d+', line)))[::-1]
        while any(numbers):
            solution += numbers[-1]
            numbers = [second - first for first, second in zip(numbers, numbers[1:])]
    return solution


if __name__ == "__main__":
    print(f"Part 1: {part_1(read_input(test=False))}")
    print(f"Part 2: {part_2(read_input(test=False))}")
