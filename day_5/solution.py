"""Day 5 solution."""
import re
from dataclasses import dataclass

from helpers import flatten, grouped, read_input, timeit


@dataclass
class SeedRange:
    start: int
    range: int

    def __init__(self, start: int, range: int):
        self.start = start
        self.range = range

    def __lt__(self, other):
        return self.start < other.start


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

    def map_ranges(self, seed_range: SeedRange) -> list[SeedRange]:
        for mr in self.mapping_ranges:
            if seed_range.start in mr:
                if seed_range.start + seed_range.range in mr:
                    # E.g. we try to map the SeedRange(1, 2) through the MappingRange(11, 0, 3),
                    # then 1 -> 12, 2 -> 13, thus returning the new SeedRange(12, 2) suffices.
                    return [
                        SeedRange(
                            mr.get_destination(seed_range.start), seed_range.range
                        )
                    ]
                else:
                    # E.g. we try to map the SeedRange(1, 5) through the MappingRange(11, 0, 3),
                    # then 1 -> 12, 2 -> 13, but 3, 4, and 5 are not in the range,
                    # thus add SeedRange(12, 2) to result and continue trying to map SeedRange(3, 3).
                    range_included = mr.range_length - (
                        seed_range.start - mr.source_range_start
                    )
                    return flatten(
                        [
                            SeedRange(
                                mr.get_destination(seed_range.start), range_included
                            ),
                            self.map_ranges(
                                SeedRange(
                                    seed_range.start + range_included,
                                    seed_range.range - range_included,
                                )
                            ),
                        ]
                    )
        # If we have run out of MappingRanges, simply return the SeedRange itself.
        return [seed_range]


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


def get_lowest_location_ranges(seeds: list[int], maps: MapList) -> int:
    seeds: list[SeedRange] = [
        SeedRange(start, range) for start, range in grouped(seeds, 2)
    ]
    current_map = maps["seed"]
    while current_map:
        new_seeds = []
        for seed_range in seeds:
            new_seeds.extend(current_map.map_ranges(seed_range))
        current_map = maps.get_next(current_map)
        seeds = new_seeds
    return min(seeds).start


def parse_maps(text: str) -> tuple[list[int], MapList]:
    tmp = re.findall(r"([^\n]+)\n([\d\s]+)", text)
    seeds = list(map(int, re.findall(r"\d+", tmp[0][0])))
    maps = MapList([Map(m[0], m[1]) for m in tmp[1:]])
    return seeds, maps


@timeit
def part_1(text: str) -> int:
    """Solution to part 1."""
    seeds, maps = parse_maps(text)
    return get_lowest_location(seeds, maps)


@timeit
def part_2(text: str) -> int:
    """Solution to part 2."""
    seeds, maps = parse_maps(text)
    return get_lowest_location_ranges(seeds, maps)


if __name__ == "__main__":
    print(f"Part 1: {part_1(read_input(single_string=True, test=False))}")
    print(f"Part 2: {part_2(read_input(single_string=True, test=False))}")
