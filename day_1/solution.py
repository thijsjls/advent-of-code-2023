"""Day 1 solution."""


def get_digit(line: str) -> int:
    """Get the first digit in a string as an int."""
    for char in line:
        if char.isdigit():
            return int(char)


def get_digit_or_word(line: str) -> int:
    """Get the first digit or written out version of a digit in a string as an int."""
    word2number = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    word = ""
    for char in line:
        word += char
        for spelled_out_digit in word2number.keys():
            if spelled_out_digit in word or spelled_out_digit in word[::-1]:
                return word2number[spelled_out_digit]
        if char.isdigit():
            return int(char)


def part_1(lines: list[str]) -> int:
    """Solution to part 1."""
    solution = 0
    for line in lines:
        solution += get_digit(line) * 10
        solution += get_digit(line[::-1])
    return solution


def part_2(lines: list[str]) -> int:
    """Solution to part 2."""
    solution = 0
    for line in lines:
        solution += get_digit_or_word(line) * 10
        solution += get_digit_or_word(line[::-1])
    return solution


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
        print(f"Part 1: {part_1(lines)}")
        print(f"Part 2: {part_2(lines)}")
