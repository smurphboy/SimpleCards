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


@pytest.mark.parametrize("string_input, ranks, suits, length", [("4D,6S", [4,6],["Diamonds", "Spades"], 2),
                                                        ("9C,AH", [9,14], ["Clubs", "Hearts"], 2),
                                                        ("8C,9S,AD", [8, 9, 14], ["Clubs", "Spades", "Diamonds"], 3)])


def test_two_cardt(string_input, ranks, suits, length):
    assert len(parse_cards(string_input)) == length
    assert all([a==b for a, b in zip((c.rank for c in parse_cards(string_input)), ranks)])
    assert all([a==b for a, b in zip((c.suit for c in parse_cards(string_input)), suits)])