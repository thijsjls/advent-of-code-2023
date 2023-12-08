"""Day 8 solution."""
from math import lcm
from helpers import read_input, timeit


def parse_nodes(lines: list[str]) -> tuple[list[int], dict[str, tuple[str, str]]]:
    return (
        [1 if char == "R" else 0 for char in lines[0].replace("\n", "")],
        {line[:3]: (line[7:10], line[12:15]) for line in lines[2:]},
    )


@timeit
def part_1(lines: list[str]) -> int:
    """Solution to part 1."""
    lr, nodes = parse_nodes(lines)
    step = 0
    node = "AAA"
    while node != "ZZZ":
        node = nodes[node][lr[step % len(lr)]]
        step += 1
    return step


@timeit
def part_2(lines: list[str]) -> int:
    """Solution to part 2."""
    lr, nodes = parse_nodes(lines)
    step = 0
    steps_per_node = []
    current_nodes = [n for n in nodes.keys() if n.endswith("A")]
    while current_nodes:
        idx_done = [i for i, n in enumerate(current_nodes) if n.endswith("Z")]
        if idx_done:
            for _ in idx_done:
                steps_per_node.append(step)
            current_nodes = [
                cn for i, cn in enumerate(current_nodes) if i not in idx_done
            ]
        current_nodes = [nodes[n][lr[step % len(lr)]] for n in current_nodes]
        step += 1
    return lcm(*steps_per_node)


if __name__ == "__main__":
    print(f"Part 1: {part_1(read_input())}")
    print(f"Part 2: {part_2(read_input())}")
