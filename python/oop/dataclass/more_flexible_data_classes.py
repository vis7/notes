from dataclasses import dataclass, field
from typing import List


@dataclass
class PlayingCard:
    rank: str
    suit: str

    def __str__(self):
        return f'{self.suit}{self.rank}'


# # simple deck containing only two cards
# @dataclass
# class Deck:
#     cards: List[PlayingCard]
#
#
# heart_of_queen = PlayingCard("Q", "Hearts")
# heart_of_king = PlayingCard("K", "Hearts")
#
# deck = Deck([heart_of_queen, heart_of_king])
# print(deck)



# Creating deck using function
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()


def make_french_deck():
    return [PlayingCard(r,s) for s in SUITS for r in RANKS]

@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

    def __repr__(self):
        cards = ', '.join(f'{c}' for c in self.cards)
        return f"{self.__class__.__name__}({cards})"

print(Deck())
