import pytest
from ..simpledeck.simpledeck import Card, check_four_of_a_kind, check_full_house, check_two_pairs, check_pair

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

def test_fourt(four_hand):
    assert check_four_of_a_kind(four_hand) == True

def test_fourf(three_hand):
    assert check_four_of_a_kind(three_hand) != True

def test_full_houset(three_hand):
    assert check_full_house(three_hand) == True

def test_full_housef(four_hand):
    assert check_full_house(four_hand) != True

def test_two_pairst(three_hand):
    assert check_two_pairs(three_hand) == True

def test_two_pairsf(four_hand):
    assert check_two_pairs(four_hand) != True

def test_pairt(three_hand):
    assert check_pair(three_hand) == True

def test_pairf(no_pair):
    assert check_pair(no_pair) != True