"""Day 6 solution."""
import re

from helpers import prod, read_input, timeit


def sim_races(times: list[int], distances: list[int]) -> int:
    race_wins = [0 for _ in times]
    for race_idx, time in enumerate(times):
        for t in range(time):
            if t * (time - t) > distances[race_idx]:
                race_wins[race_idx] += 1
    return prod(race_wins)


@timeit
def part_1(lines: list[str]) -> int:
    """Solution to part 1."""
    times = list(map(int, re.findall(r"\d+", lines[0])))
    distances = list(map(int, re.findall(r"\d+", lines[1])))
    return sim_races(times, distances)


@timeit
def part_2(lines: list[str]) -> int:
    """Solution to part 2."""
    times = [int("".join(re.findall(r"\d+", lines[0])))]
    distances = [int("".join(re.findall(r"\d+", lines[1])))]
    return sim_races(times, distances)


if __name__ == "__main__":
    print(f"Part 1: {part_1(read_input())}")
    print(f"Part 2: {part_2(read_input())}")
