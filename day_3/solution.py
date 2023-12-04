"""Day 3 solution."""

import re
from dataclasses import dataclass


@dataclass
class Coordinate:
    x: int
    y: int


@dataclass
class Number:
    value: int
    coordinates: list[Coordinate]


def read_input(test: bool = False) -> list[str]:
    """Read input file lines."""
    input_file = "input.txt"
    if test:
        input_file = "test_input.txt"
    with open(input_file, "r") as f:
        lines = f.readlines()
        return lines


def get_symbols(lines: list[str]) -> list[Coordinate]:
    symbols = []
    for y, line in enumerate(lines):
        symbols.extend(
            Coordinate(match.start(), y)
            for match in re.finditer(r'[^\w\s.]', line)
        )
    return symbols


def get_star_symbols(lines: list[str]) -> list[Coordinate]:
    symbols = []
    for y, line in enumerate(lines):
        symbols.extend(
            Coordinate(match.start(), y)
            for match in re.finditer(r'[*]', line)
        )
    return symbols


def get_numbers(lines: list[str]) -> list[Number]:
    numbers = []
    for y, line in enumerate(lines):
        numbers.extend(
            Number(
                int(match.group()),
                [
                    Coordinate(x, y)
                    for x in range(match.span()[0], match.span()[1])
                ]
            )
            for match in re.finditer(r'\b\d+\b', line)
        )
    return numbers


def is_part_number(num: Number, symbols: list[Coordinate]) -> bool:
    for co in num.coordinates:
        if is_adjacent(co, symbols):
            return True
    return False


def is_gear(potential_gear: Coordinate, numbers: list[Number]) -> int:
    """If a '*' symbol is a gear, return its ratio. Return 0 otherwise."""
    num_numbers = 0
    gear_ratio = 1
    for num in numbers:
        if is_adjacent(potential_gear, num.coordinates):
            num_numbers += 1
            gear_ratio *= num.value
    if num_numbers == 2:
        return gear_ratio
    return 0


def is_adjacent(co: Coordinate, coordinates: list[Coordinate]) -> bool:
    for x in [co.x - 1, co.x, co.x + 1]:
        for y in [co.y - 1, co.y, co.y + 1]:
            if Coordinate(x, y) in coordinates:
                return True
    return False


def part_1(lines: list[str]) -> int:
    """Solution to part 1."""
    solution = 0
    symbols = get_symbols(lines)
    numbers = get_numbers(lines)
    for num in numbers:
        if is_part_number(num, symbols):
            solution += num.value
    return solution


def part_2(lines: list[str]) -> int:
    """Solution to part 2."""
    solution = 0
    potential_gears = get_star_symbols(lines)
    numbers = get_numbers(lines)
    for pg in potential_gears:
        solution += is_gear(pg, numbers)
    return solution


if __name__ == "__main__":
    print(f"Part 1: {part_1(read_input(test=False))}")
    print(f"Part 2: {part_2(read_input(test=False))}")
