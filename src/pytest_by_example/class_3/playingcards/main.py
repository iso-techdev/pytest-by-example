from card import Card
from deck import Deck

# Card Generated Using Deck
player_deck = Deck()
player_card = player_deck.draw_card()
player_hand = player_deck.draw_n(1)

# Card Generated From Instantiation
player_card_2 = Card()

print(player_hand)
