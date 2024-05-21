import pytest
from simpledeck import Deck, Card, check_flush, check_straight, scorehand

hand = []
hand.append(Card(4, 'Diamonds'))
hand.append(Card(5, 'Hearts'))
hand.append(Card(6, 'Spades'))
hand.append(Card(8, 'Spades'))
hand.append(Card(12, 'Clubs'))
hand.append(Card(2, 'Hearts'))
hand.append(Card(3, 'Hearts'))

assert check_flush(hand) != True, f'Only 3 hearts, not a flush'
assert check_flush(hand, 3) == True, f'3 Hearts so a 3 card flush'
assert check_straight(hand) == True, f'5 card straight'
