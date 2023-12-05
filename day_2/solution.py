"""Day 2 solution."""


def read_input(test: bool = False) -> list[str]:
    """Read input file lines."""
    input_file = "input.txt"
    if test:
        input_file = "test_input.txt"
    with open(input_file, "r") as f:
        lines = f.readlines()
        return lines


def game_is_possible(game: str, bag: dict) -> bool:
    """Determine whether a single game breaks the bag violations."""
    for subset in game.split(":")[1].split(";"):
        for cubes in subset.split(","):
            number = int(cubes.split(" ")[1])
            color = cubes.split(" ")[2].replace("\n", "")
            if number > bag[color]:
                return False
    return True


def prod(l: list) -> int:
    result = 1
    for e in l:
        result *= e
    return result


def possible_bags(game: str) -> dict:
    """Get all the possible bags from a game."""
    bags = {"red": [], "green": [], "blue": []}
    for subset in game.split(":")[1].split(";"):
        for cubes in subset.split(","):
            number = int(cubes.split(" ")[1])
            color = cubes.split(" ")[2].replace("\n", "")
            bags[color].append(number)
    return bags


def minimal_bag(bags: dict) -> list:
    """Get the minimal bag out of a set of possible bags."""
    return [max(bags["red"]), max(bags["green"]), max(bags["blue"])]


def part_1(lines: list[str]) -> int:
    """Solution to part 1."""
    solution = 0
    bag = {"red": 12, "green": 13, "blue": 14}
    for id, game in enumerate(lines):
        if game_is_possible(game, bag):
            solution += id + 1
    return solution


def part_2(lines: list[str]) -> int:
    """Solution to part 2."""
    solution = 0
    for game in lines:
        bags = possible_bags(game)
        solution += prod(minimal_bag(bags))
    return solution


if __name__ == "__main__":
    print(f"Part 1: {part_1(read_input(test=False))}")
    print(f"Part 2: {part_2(read_input(test=False))}")
