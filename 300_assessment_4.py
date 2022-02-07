"""
Deck Class
-|-|-|-|-|-

Create a [Deck] class that represents a desk of [52] playing cards
The [Deck] should maintain which cards are currently in the deck and never contain duplicated cards. 
Cards should be represented by their value (2 -10, J, Q, K, A) followed by a suit (D, H, C, S)

Your [Deck] class should implement following methods: 
- [shuffle()] = randomise the cards

 [deal(n)] = removes and returns the last [n] cards from the deck in a list
-- if the deck does not contain enough cards, it returns all the cards in the deck 

- [sort_by_suit()] = sort cards by suit, placing Hearts first, diamonds, clubs, spades.
-- the order within each suit does not matter
-- sort, do not return 

- [contains_card(card)] = return [True] if a given card exists in deck and [False] if not

- [copy()] = return a new [Deck] object that is a copy of the current deck
-- any modification made to the new [Deck] should not affect the [Deck] object that was copied

- [get_cards()] = returns all the cards in the deck in a list
-- any modifications to the returned list should not change the [Deck] object 

- [__len__()] = returns number of cards in the [Deck]

__________________________________

[Deck] should always start with exactly [52] cards distributed across [4] suites and [13] values where there are no duplicates
"""

