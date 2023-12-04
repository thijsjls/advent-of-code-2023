"""Day 4 solution."""


def read_input(test: bool = False) -> list[str]:
    """Read input file lines."""
    input_file = "input.txt"
    if test:
        input_file = "test_input.txt"
    with open(input_file, "r") as f:
        lines = f.readlines()
        return lines


def part_1(lines: list[str]) -> int:
    """Solution to part 1."""
    solution = 0
    return solution


def part_2(lines: list[str]) -> int:
    """Solution to part 2."""
    solution = 0
    return solution


if __name__ == "__main__":
    print(f"Part 1: {part_1(read_input(test=True))}")
    print(f"Part 2: {part_2(read_input(test=True))}")
