from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank: str = "A"
    suit: str = "Spades"

queen_of_hearts = DataClassCard("Q", "Hearts")
print(queen_of_hearts)
print(queen_of_hearts.rank)
print(queen_of_hearts.suit)

# creating card from default value
card = DataClassCard()
print(card)
print(card.rank)
print(card.suit)

king_of_hearts = DataClassCard(10, 20)
print(king_of_hearts)
print(king_of_hearts.rank)
print(king_of_hearts.suit)



## data class
# It provide default constructor, So we did't need to write it
# It provide __repr__ and __eq__ method implimentation by default
# we need to specify type of variable in data class, but as python is and will always be dynamically typed languange we can assign other datatypes too
# data class is just a regular class. That means that you can freely add your own methods to a data class.
