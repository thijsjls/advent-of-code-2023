"""Day 9 solution."""
import re

from helpers import read_input, timeit


def extrapolate(numbers: list[int]) -> int:
    result = 0
    while any(numbers):
        result += numbers[-1]
        numbers = [second - first for first, second in zip(numbers, numbers[1:])]
    return result


@timeit
def part_1(lines: list[str]) -> int:
    """Solution to part 1."""
    return sum(
        extrapolate(list(map(int, re.findall(r"-?\d+", line)))) for line in lines
    )


@timeit
def part_2(lines: list[str]) -> int:
    """Solution to part 2."""
    return sum(
        extrapolate(list(map(int, re.findall(r"-?\d+", line)))[::-1]) for line in lines
    )


if __name__ == "__main__":
    print(f"Part 1: {part_1(read_input(test=False))}")
    print(f"Part 2: {part_2(read_input(test=False))}")
