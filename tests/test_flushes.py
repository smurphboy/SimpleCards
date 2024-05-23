import pytest
from ..simpledeck.simpledeck import Card, check_flush, check_straight, check_straight_flush, check_royal_flush
@pytest.fixture
def flush_hand():
    '''makes a sample hand for testing flushes and straights'''
    hand = []
    hand.append(Card(4, 'Diamonds'))
    hand.append(Card(5, 'Hearts'))
    hand.append(Card(6, 'Spades'))
    hand.append(Card(8, 'Spades'))
    hand.append(Card(12, 'Clubs'))
    hand.append(Card(2, 'Hearts'))
    hand.append(Card(3, 'Hearts'))
    return hand

@pytest.fixture
def sflush_hand():
    '''makes a sample hand for testing straight flushes'''
    hand = []
    hand.append(Card(4, 'Hearts'))
    hand.append(Card(5, 'Hearts'))
    hand.append(Card(6, 'Hearts'))
    hand.append(Card(8, 'Spades'))
    hand.append(Card(12, 'Clubs'))
    hand.append(Card(2, 'Hearts'))
    hand.append(Card(3, 'Hearts'))
    return hand

@pytest.fixture
def rflush_hand():
    '''makes a sample hand for testing Royal Flushes'''
    hand = []
    hand.append(Card(12, 'Hearts'))
    hand.append(Card(11, 'Hearts'))
    hand.append(Card(10, 'Hearts'))
    hand.append(Card(8, 'Spades'))
    hand.append(Card(12, 'Clubs'))
    hand.append(Card(13, 'Hearts'))
    hand.append(Card(14, 'Hearts'))
    return hand

def test_flushes(flush_hand):
    assert check_flush(flush_hand) != True, f'Only 3 hearts, not a flush'
    assert check_flush(flush_hand, 3) == True, f'3 Hearts so a 3 card flush'

def test_straights(flush_hand):
    assert check_straight(flush_hand) == True, f'5 card straight'

def test_straight_flush(sflush_hand):
    assert check_straight_flush(sflush_hand) == True, f'Heart Flush to the 6'

def test_royal_flushf(sflush_hand):
    assert check_royal_flush(sflush_hand) != True, f'Flush to the Ace'

def test_royal_flusht(rflush_hand):
    assert check_royal_flush(rflush_hand) == True, f'Flush to the Ace'
