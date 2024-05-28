from collections import defaultdict
from itertools import product, combinations
import random


class Card(object):

    FACES = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        value = self.FACES.get(self.rank, self.rank)
        return "{0} of {1}".format(value, self.suit)

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

    def __init__(self, name, order, handsize=11):
        self.name = name
        self.order = order # player 1 or player 2, etc.


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

PLAYERS = 2
HANDSIZE = 11
SCORINGHAND = 5
TARGET = 500

if __name__ == '__main__':
    mydeck = Deck()
    mydeck.shuffle()
    player_list = []
    for idx, player in enumerate(range(PLAYERS)):
        player = Player(f"Player {idx}", idx, HANDSIZE)
        player.hand = mydeck.deal(HANDSIZE)
        player_list.append(player)
        print(f"{player.name} has {len(player.hand)} cards in hand")
        print(" - ".join(map(str, player.hand)))
        print(f"Best Hand: {besthand(player.hand)}")    
    print(f"Cards left in deck = {len(mydeck.deck)}")
