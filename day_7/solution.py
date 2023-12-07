"""Day 7 solution."""
from dataclasses import dataclass

from helpers import max_count, read_input, timeit

CARD_ORDER = "AKQJT98765432"
TYPE_ORDER = "Poker Four of a kind Full house Three of a kind Two pair One pair Soep"


@dataclass
class Card:
    label: str

    def __hash__(self):
        return hash(self.label)

    def __lt__(self, other):
        return CARD_ORDER.index(self.label) > CARD_ORDER.index(other.label)


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
        return TYPE_ORDER.index(self.type) > TYPE_ORDER.index(other.type)


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
    CARD_ORDER = "AKQT98765432J"
    return sum(
        (rank + 1) * h.bid
        for rank, h in enumerate(sorted([Hand(line, jokers=True) for line in lines]))
    )


if __name__ == "__main__":
    print(f"Part 1: {part_1(read_input())}")
    print(f"Part 2: {part_2(read_input())}")
