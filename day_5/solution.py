"""Day 5 solution."""
import re
from dataclasses import dataclass

from helpers import grouped, read_input, timeit


@dataclass
class MappingRange:
    destination_range_start: int
    source_range_start: int
    range_length: int

    def __init__(self, line: str):
        self.destination_range_start, self.source_range_start, self.range_length = map(
            int, re.findall(r"\d+", line)
        )

    def __repr__(self):
        return f"{self.destination_range_start} {self.source_range_start} {self.range_length}"

    def __contains__(self, source: int) -> bool:
        return (
            self.source_range_start
            <= source
            < self.source_range_start + self.range_length
        )

    def get_destination(self, source: int) -> int | None:
        if source in self:
            return (source - self.source_range_start) + self.destination_range_start
        print(f"Error: Source {source} not in MappingRange: {self}")


@dataclass
class Map:
    source_name: str
    destination_name: str
    mapping_ranges: list[MappingRange]

    def __init__(self, name: str, mapping_ranges: str):
        self.source_name, _, self.destination_name = name[:-5].split("-")
        self.mapping_ranges = [
            MappingRange(mr) for mr in re.findall(r"\n*([\d ]+)\n", mapping_ranges)
        ]

    def map(self, source: int) -> int:
        for mr in self.mapping_ranges:
            if source in mr:
                return mr.get_destination(source)
        return source

    def get_lowest_range(self) -> MappingRange:
        zero_mapping = False
        lowest_range = None
        lowest_destination_range_start = 10**100
        lowest_source_range_start = 10**100
        for mr in self.mapping_ranges:
            if mr.source_range_start == 0:
                zero_mapping = True
            if mr.destination_range_start < lowest_destination_range_start:
                lowest_range = mr
                lowest_destination_range_start = mr.destination_range_start
            if mr.source_range_start < lowest_source_range_start:
                lowest_source_range_start = mr.source_range_start
        if zero_mapping:
            return lowest_range
        return MappingRange(f"{0} {0} {lowest_source_range_start}")


@dataclass
class MapList:
    map_list = list[Map]

    def __init__(self, map_list: list[Map]):
        self.map_list = map_list

    def __getitem__(self, source: str) -> Map:
        for m in self.map_list:
            if m.source_name == source:
                return m

    def get_next(self, map: Map) -> Map:
        for m in self.map_list:
            if m.source_name == map.destination_name:
                return m

    def get_previous(self, map: Map) -> Map:
        for m in self.map_list:
            if m.destination_name == map.source_name:
                return m


def get_lowest_location(seeds: list[int], maps: MapList) -> int:
    current_map = maps["seed"]
    while current_map:
        for i, num in enumerate(seeds):
            seeds[i] = current_map.map(num)
        current_map = maps.get_next(current_map)
    return min(seeds)


def get_lowest_range(seeds: list[int], maps: MapList) -> MappingRange:
    current_map = maps["humidity"]
    while current_map:
        lowest = current_map.get_lowest_range()
        current_map = maps.get_previous(current_map)
    return lowest


def parse_maps(text: str) -> tuple[list[int], MapList]:
    tmp = re.findall(r"([^\n]+)\n([\d\s]+)", text)
    seeds = list(map(int, re.findall(r"\d+", tmp[0][0])))
    maps = MapList([Map(m[0], m[1]) for m in tmp[1:]])
    return seeds, maps


def parse_seeds(seeds: list[int]) -> list[int]:
    new_seeds = []
    for start, length in grouped(seeds, 2):
        new_seeds.extend(list(range(start, start + length)))
    return new_seeds


@timeit
def part_1(text: str) -> int:
    """Solution to part 1."""
    seeds, maps = parse_maps(text)
    return get_lowest_location(seeds, maps)


@timeit
def part_2(text: str) -> int:
    """Solution to part 2."""
    seeds, maps = parse_maps(text)
    return 0


if __name__ == "__main__":
    print(f"Part 1: {part_1(read_input(single_string=True, test=True))}")
    print(f"Part 2: {part_2(read_input(single_string=True, test=True))}")
