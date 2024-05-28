import pytest
from ..simpledeck.simpledeck import Card, besthand

@pytest.fixture
def four_hand():
    '''makes a sample hand for testing 4 of a Kind'''
    hand = []
    hand.append(Card(12, 'Hearts'))
    hand.append(Card(11, 'Hearts'))
    hand.append(Card(10, 'Hearts'))
    hand.append(Card(12, 'Spades'))
    hand.append(Card(12, 'Clubs'))
    hand.append(Card(13, 'Hearts'))
    hand.append(Card(12, 'Diamonds'))
    return hand

@pytest.fixture
def three_hand():
    '''makes a sample hand for testing 3 of a Kind and full house'''
    hand = []
    hand.append(Card(12, 'Hearts'))
    hand.append(Card(7, 'Hearts'))
    hand.append(Card(7, 'Diamonds'))
    hand.append(Card(2, 'Spades'))
    hand.append(Card(2, 'Clubs'))
    hand.append(Card(3, 'Hearts'))
    hand.append(Card(2, 'Diamonds'))
    return hand

@pytest.fixture
def no_pair():
    '''makes a sample hand for testing pairs'''
    hand = []
    hand.append(Card(12, 'Hearts'))
    hand.append(Card(11, 'Hearts'))
    hand.append(Card(7, 'Diamonds'))
    hand.append(Card(2, 'Spades'))
    hand.append(Card(9, 'Clubs'))
    hand.append(Card(3, 'Hearts'))
    hand.append(Card(4, 'Diamonds'))
    return hand

def test_4oak(four_hand):
    assert besthand(four_hand) == "Four of a Kind"

def test_hc(no_pair):
    assert besthand(no_pair) == "High Card"