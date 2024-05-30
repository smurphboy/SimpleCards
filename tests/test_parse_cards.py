import pytest
from ..simpledeck.simpledeck import Card, parse_cards


@pytest.mark.parametrize("test_input, rank, suit",[("4D", 4, "Diamonds"),
                                                  ("6S", 6, "Spades"),
                                                  ("9C", 9, "Clubs"),
                                                  ("AH", 14, "Hearts"),
                                                  ("13C", 13, "Clubs"),
                                                  ("KC", 13, "Clubs")])

def test_single_cardt(test_input, rank, suit):
    assert parse_cards(test_input)[0].rank == rank
    assert parse_cards(test_input)[0].suit == suit