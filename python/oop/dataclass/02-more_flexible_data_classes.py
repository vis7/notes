from dataclasses import dataclass, field, fields
from typing import List, Tuple


@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                           + SUITS.index(self.suit))

    def __str__(self):
        return f'{self.suit}{self.rank} {self.sort_index}'


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

# print(Deck())
# print(fields(Deck))



# The field() specifier is used to customize each field of a data class individually. You will see some other examples later. For reference, these are the parameters field() supports:
#
# default: Default value of the field
# default_factory: Function that returns the initial value of the field
# init: Use field in .__init__() method? (Default is True.)
# repr: Use field in repr of the object? (Default is True.)
# compare: Include the field in comparisons? (Default is True.)
# hash: Include the field when calculating hash()? (Default is to use the same as for compare.)
# metadata: A mapping with information about the field


# queen_of_hearts = PlayingCard("Q", "♡")
# ace_of_spades = PlayingCard("A", "♠")
#
# print(ace_of_spades > queen_of_hearts)

# The @dataclass decorator has two forms. So far you have seen the simple form where @dataclass is specified without any parentheses and parameters. However, you can also give parameters to the @dataclass() decorator in parentheses. The following parameters are supported:
#
# init: Add .__init__() method? (Default is True.)
# repr: Add .__repr__() method? (Default is True.)
# eq: Add .__eq__() method? (Default is True.)
# order: Add ordering methods? (Default is False.)
# unsafe_hash: Force the addition of a .__hash__() method? (Default is False.)
# frozen: If True, assigning to fields raise an exception. (Default is False.)

# sorted deck
# print(Deck(sorted(make_french_deck())))


@dataclass(frozen=True)
class ImmutableCard:
    rank: str
    suit: str

@dataclass(frozen=True)
class ImmutableDeck:
    cards: List[ImmutableCard]

queen_of_hearts = ImmutableCard("Q", "♡")
ace_of_spades = ImmutableCard("A", "♠")

deck = ImmutableDeck([queen_of_hearts, ace_of_spades])
deck.cards[0] = ImmutableCard("7", "♠")
print(deck)
