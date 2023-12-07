"""Day 7 solution."""
from dataclasses import dataclass

from helpers import max_count, read_input, timeit

CARD_ORDER = {
    "A": 0,
    "K": 1,
    "Q": 2,
    "J": 3,
    "T": 4,
    "9": 5,
    "8": 6,
    "7": 7,
    "6": 8,
    "5": 9,
    "4": 10,
    "3": 11,
    "2": 12,
}

TYPE_ORDER = {
    "Poker": 0,
    "Four of a kind": 1,
    "Full house": 2,
    "Three of a kind": 3,
    "Two pair": 4,
    "One pair": 5,
    "Soep": 6,
}


@dataclass
class Card:
    label: str

    def __hash__(self):
        return hash(self.label)

    def __lt__(self, other):
        return CARD_ORDER[self.label] > CARD_ORDER[other.label]

    def __gt__(self, other):
        return CARD_ORDER[self.label] < CARD_ORDER[other.label]


@dataclass
class Hand:
    cards: list[Card]
    bid: int
    type: str

    def __init__(self, input: str, jokers: bool = False):
        cards, bid = input.split()
        self.cards = [Card(c) for c in cards]
        self.bid = int(bid)
        self.type = self._get_type(jokers)

    def _get_type(self, jokers: bool) -> str:
        cards = self.cards
        if jokers:
            if cards == [Card("J") for _ in range(5)]:
                return "Poker"
            best_card = max(set(c for c in cards if c != Card("J")), key=cards.count)
            cards = [best_card if c == Card("J") else c for c in cards]
        match len(set(cards)):
            case 1:
                return "Poker"
            case 2:
                if max_count(cards) == 4:
                    return "Four of a kind"
                return "Full house"
            case 3:
                if max_count(cards) == 3:
                    return "Three of a kind"
                return "Two pair"
            case 4:
                return "One pair"
            case 5:
                return "Soep"

    def __eq__(self, other):
        return self.cards == other.cards

    def __lt__(self, other):
        if self.type == other.type:
            for i, card in enumerate(self.cards):
                if card > other.cards[i]:
                    return False
                elif card < other.cards[i]:
                    return True
            return False
        return TYPE_ORDER[self.type] > TYPE_ORDER[other.type]

    def __gt__(self, other):
        return not (self < other or self == other)


@timeit
def part_1(lines: list[str]) -> int:
    """Solution to part 1."""
    return sum(
        (rank + 1) * h.bid
        for rank, h in enumerate(sorted([Hand(line) for line in lines]))
    )


@timeit
def part_2(lines: list[str]) -> int:
    """Solution to part 2."""
    CARD_ORDER["J"] = 13
    return sum(
        (rank + 1) * h.bid
        for rank, h in enumerate(sorted([Hand(line, jokers=True) for line in lines]))
    )


if __name__ == "__main__":
    print(f"Part 1: {part_1(read_input())}")
    print(f"Part 2: {part_2(read_input())}")
