"""Day 4 solution."""
from collections import defaultdict
import time


def timeit(f):

    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print(f"func:{f.__name__} took: {te-ts} sec")
        return result

    return timed


def read_input(test: bool = False) -> list[str]:
    """Read input file lines."""
    input_file = "input.txt"
    if test:
        input_file = "test_input.txt"
    with open(input_file, "r") as f:
        lines = f.readlines()
        return lines


def parse_card(line: str) -> tuple[set[str]]:
    tmp = line.replace('\n', '').split(':')[1].split('|')
    return set(tmp[0].split()), set(tmp[1].split())


@timeit
def part_1(lines: list[str]) -> int:
    """Solution to part 1."""
    solution = 0
    for line in lines:
        winning_numbers, numbers_you_have = parse_card(line)
        overlap = winning_numbers.intersection(numbers_you_have)
        solution += 2**(len(overlap)-1) if overlap else 0
    return solution


@timeit
def part_2(lines: list[str]) -> int:
    """Solution to part 2."""
    solution = 0
    cards = defaultdict(int)
    for card_num, line in enumerate(lines):
        cards[card_num] += 1
        solution += 1
        for _ in range(cards[card_num]):
            winning_numbers, numbers_you_have = parse_card(line)
            for i in range(len(winning_numbers.intersection(numbers_you_have))):
                cards[card_num + i + 1] += 1
                solution += 1
    return solution


if __name__ == "__main__":
    print(f"Part 1: {part_1(read_input(test=False))}")
    print(f"Part 2: {part_2(read_input(test=False))}")
