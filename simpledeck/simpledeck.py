from collections import defaultdict
from itertools import product, combinations
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.columns import Columns
import random
import re



class Card(object):

    FACES = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        value = self.FACES.get(self.rank, self.rank)
        if self.suit in ["Hearts", "Diamonds"]:
            self.colour = "red"
        else:
            self.colour = "black"
        return "[bold]{0}[/bold] of [bold {2}]{1}[/bold {2}]".format(value, self.suit, self.colour)

    def __lt__(self, other):
        return self.rank < other.rank


class Deck(object):

    def __init__ (self, ranks=None, suits=None):
        if ranks is None:
            ranks = range(2, 15)
        if suits is None:
            suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.deck = [Card(r, s) for r, s in product(ranks, suits)]
        self.length = len(ranks) * len(suits)

    def __len__ (self):
        return self.length

    def shuffle(self):
        return random.shuffle(self.deck)

    def deal(self, n):
        dealt = []
        for i in range(n):
            dealt.append(self.deck.pop())
        return dealt


class Player(object):

    def __init__(self, name, order, deck, handsize=11):
        self.name = name
        self.order = order # player 1 or player 2, etc.
        self.hand = deck.deal(HANDSIZE)


def check_flush(hand, size=5):
    '''checks for size (five by default) card flush in given hand'''
    if len(hand) < size:
        return False
    for subhand in combinations(hand, size):
        suits = [h.suit for h in subhand]
        if len(set(suits)) == 1:
            return True
    return False

def check_straight(hand, size=5):
    '''check for size (five by default) card straight in a given hand. 
       includes A, 2, 3, 4, 5 as well as 10, J, Q, K, A'''
    for subhand in combinations(hand, size):
        values = [i.rank for i in subhand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v] += 1
        value_range = max(values) - min(values)
        if len(set(value_counts.values())) == 1 and (value_range==4):
            return True
        else:
            #check straight with low Ace
            if set(values) == set([14, 2, 3, 4, 5]):
                return True
    return False

def check_straight_flush(hand, size=5):
    for subhand in combinations(hand, size):
        if check_flush(subhand) and check_straight(subhand):
            return True
    return False

def check_royal_flush(hand, size=5):
    for subhand in combinations(hand, size):
        if check_straight_flush(subhand):
            values = [i.rank for i in subhand]
            if set(values) == set([14, 13, 12, 11, 10]):
                return True
    return False

def check_four_of_a_kind(hand, size=5):
    for subhand in combinations(hand, size):
        values = [i.rank for i in subhand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if sorted(value_counts.values()) == [1,4]:
            return True
    return False

def check_three_of_a_kind(hand, size=5):
    for subhand in combinations(hand, size):
        values = [i.rank for i in subhand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if set(value_counts.values()) == set([3,1]):
            return True
    return False

def check_full_house(hand, size=5):
    for subhand in combinations(hand, size):
        values = [i.rank for i in subhand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if sorted(value_counts.values()) == [2,3]:
            return True
    return False

def check_two_pairs(hand, size=5):
    for subhand in combinations(hand, size):
        values = [i.rank for i in subhand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if sorted(value_counts.values())==[1,2,2]:
            return True
    return False

def check_pair(hand, size=5):
    for subhand in combinations(hand, size):
        values = [i.rank for i in hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if 2 in value_counts.values():
            return True
    return False

def besthand(hand):
    '''returns best poker hand from hand supplied'''
    if check_flush(hand):
        if check_straight(hand):
            if check_royal_flush(hand):
                return "Royal Flush"
            if check_straight_flush(hand):
                return "Straight Flush"
        if check_four_of_a_kind(hand):
            return "Four of a kind"
        if check_full_house(hand):
            return "Full House"
        return "Flush"
    if check_four_of_a_kind(hand):
        return "Four of a Kind"
    if check_full_house(hand):
        return "Full House"
    if check_three_of_a_kind(hand):
        return "Three of a Kind"
    if check_two_pairs(hand):
        return "Two Pairs"
    if check_pair(hand):
        return "Pair"
    return "High Card"

def parse_cards(input_string:str):
    '''Parses the input string and returns the cards contained'''
    SUITS = {"C": "Clubs", "D" : "Diamonds", "H": "Hearts", "S": "Spades"}
    FACERANKS = {"J" : 11, "Q" : 12, "K" : 13, "A" : 14}
    raw_cards = input_string.split(",")
    print(f"[bold]{len(raw_cards)}[/bold] cards detected")
    clean_cards = []
    for card in raw_cards:
        proposed_card = card.strip()
        if (len(proposed_card) == 2) or (len(proposed_card) == 3): # right length
            if proposed_card[0].isdigit(): # we have a number
                proposed_rank = int(re.search(r'\d+', proposed_card).group())
            else: # we have a letter
                if proposed_card[0] in ["J", "Q", "K", "A"]:
                    proposed_rank = FACERANKS.get(proposed_card[0])
            proposed_suit = proposed_card[-1].upper()
            proposed_suit = SUITS.get(proposed_suit)
            clean_cards.append(Card(proposed_rank,proposed_suit))
    return clean_cards


PLAYERS = 2
HANDSIZE = 11
SCORINGHAND = 5
TARGET = 500

if __name__ == '__main__':
    mydeck = Deck()
    mydeck.shuffle()
    player_list = []
    panel_list = []
    for idx, player in enumerate(range(PLAYERS)):
        player = Player(f"Player {idx}", idx, mydeck, HANDSIZE)
        player_list.append(player)
        panel_list.append(Panel("\n".join(map(str, player.hand)),
                    title=f"{player.name} - [bold]{len(player.hand)}[/bold] cards",
                    subtitle=f"Best Hand: {besthand(player.hand)}",
                    width=30))
    console=Console()
    console.print(Columns(panel_list))
    print(f"Cards left in deck = {len(mydeck.deck)}")
    for player in player_list:
        instruction = input(f"{player.name}'s Turn. Discard or Play Hand [D or P]: ")
        if instruction == ("D" or "d"):
            discard = input(f"Cards to Discard, max {SCORINGHAND}. [Rank/Suit, Rank/Suit, e.g. AS, 10D]: ")
        elif instruction == ("P" or "p"):
            played = input(f"Cards to Play, max {SCORINGHAND}. [Rank/Suit, Rank/Suit, e.g. AS, 10D]: ")
        else:
            print("Turn Passed")
        print(f"{instruction}")
