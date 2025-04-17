from enum import Enum
from dataclasses import dataclass
import random
from collections import Counter


SUITS = tuple('♣ ♢ ♡ ♠'.split())
RANKS = tuple('2 3 4 5 6 7 8 9 10 J Q K A'.split())


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.suit}{self.rank}'

    @property
    def suit_index(self):
        return SUITS.index(self.suit)

    @property
    def rank_index(self):
        return RANKS.index(self.rank)

    @staticmethod
    def from_str(card_str):
        suit = card_str[:-1]
        rank = card_str[-1:]
        return Card(suit, rank)

    @staticmethod
    def sort_key(card):
        return card.suit_index, card.rank_index


class Cards:
    def __init__(self, *cards):
        self.cards = list(cards)

    def __str__(self):
        return ' '.join([str(card) for card in self.cards])

    def __len__(self):
        return len(self.cards)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index >= len(self.cards):
            raise StopIteration
        else:
            card = self.cards[self._index]
            self._index += 1
            return card

    def add(self, *cards):
        self.cards.extend(cards)

    def take(self, number_of_cards = 1):
        return Cards(*[self.cards.pop() for _ in range(number_of_cards)])

    def sort(self):
        self.cards.sort(key = Card.sort_key)

    def suits(self):
        return [card.suit for card in self.cards]

    def ranks(self):
        return [card.rank for card in self.cards]

    @staticmethod
    def from_str(hand_str):
        cards = Cards()
        for card_str in hand_str.split():
            cards.add(Card.from_str(card_str))
        return cards


class Deck(Cards):
    def __init__(self):
        super().__init__()
        for suit in SUITS:
            for rank in RANKS:
                self.add(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)


class Hand(Cards):
    def __init__(self, *cards):
        super().__init__(*cards)
        self.sort()

    def add(self, *cards):
        super().add(*cards)
        self.sort()



class PokerCombinations(Enum):
    HIGH_CARD = 1,
    ONE_PAIR = 2,
    TWO_PAIR = 3,
    THREE_OF_A_KIND = 4,
    STRAIGHT = 5,
    FLUSH = 6,
    FULL_HOUSE = 7,
    FOUR_OF_A_KIND = 8,
    STRAIGHT_FLUSH = 9,
    ROYAL_FLUSH = 10,


class PokerCombination:

    def __init__(self, cards: Cards):
        self.cards = cards
        self.ranks_counter = dict(Counter(self.cards.ranks()))
        self.suits_counter = dict(Counter(self.cards.suits()))

    def select_used_cards(self, n1, n2=None):
        used_rank = [rank for rank, count in self.ranks_counter.items() if count == n1][0]
        used_cards = Cards(*[card for card in self.cards if card.rank == used_rank])
        if n2:
            used_rank = [rank for rank, count in self.ranks_counter.items() if count == n2][0]
            used_cards.add(*[card for card in self.cards if card.rank == used_rank])
        return str(used_cards)

    def high_card(self):
        return max(self.cards, key = lambda card: card.rank_index)

    def is_straight(self):
        indeces = sorted(RANKS.index(r) for r in self.cards.ranks())
        for i1, i2 in zip(indeces[:-1], indeces[1:]):
            if i1 + 1 != i2:
                return False
        return True

    def is_flush(self):
        return len(set(self.suits_counter.values())) == 1

    def best_combination(self):
        counts = self.ranks_counter.values()

        if any(count == 4 for count in counts):
            # print(self.select_used_cards(4))
            return PokerCombinations.FOUR_OF_A_KIND

        elif any(count == 3 for count in counts):
            if any(count == 2 for count in counts):
                # print(self.select_used_cards(3, 2))
                return PokerCombinations.FULL_HOUSE
            else:
                # print(self.select_used_cards(3))
                return PokerCombinations.THREE_OF_A_KIND

        elif any(count == 2 for count in counts):
            if len([count for count in counts if count == 2]) == 2:
                return PokerCombinations.TWO_PAIR
            else:
                return PokerCombinations.ONE_PAIR

        else:
            if self.is_straight():
                if self.is_flush():
                    if self.high_card() == 'A':
                        return PokerCombinations.ROYAL_FLUSH
                    else:
                        return PokerCombinations.STRAIGHT_FLUSH

                else:
                    return PokerCombinations.STRAIGHT

            else:
                if self.is_flush():
                    return PokerCombinations.FLUSH

                else:
                    return PokerCombinations.HIGH_CARD

# -------------------------------------------------------------------------

if __name__ == '__main__':

    deck = Deck()
    deck.shuffle()

    hand = Hand(*deck.take(5))

    # print(deck)
    print(hand)

    analyzer = PokerCombination(hand)
    print(analyzer.best_combination())

    print(f'\nTest cases:')
    print(s := '♢3 ♢4 ♢A ♡K ♠Q', PokerCombination(Cards.from_str(s)).best_combination())
    print(s := '♢4 ♢7 ♡10 ♡A ♠7', PokerCombination(Cards.from_str(s)).best_combination())
    print(s := '♣K ♢2 ♡2 ♡10 ♠K', PokerCombination(Cards.from_str(s)).best_combination())
    print(s := '♣K ♢2 ♡3 ♡K ♠K', PokerCombination(Cards.from_str(s)).best_combination())
    print(s := '♣K ♢2 ♡2 ♡K ♠K', PokerCombination(Cards.from_str(s)).best_combination())
    print(s := '♣K ♢K ♡2 ♡K ♠K', PokerCombination(Cards.from_str(s)).best_combination())
    print(s := '♢5 ♢6 ♢2 ♢J ♢K', PokerCombination(Cards.from_str(s)).best_combination())
    print(s := '♢4 ♢7 ♡5 ♡8 ♠6', PokerCombination(Cards.from_str(s)).best_combination())
    print(s := '♢4 ♢7 ♢5 ♢8 ♢6', PokerCombination(Cards.from_str(s)).best_combination())

    stats = {}
    n = 10000
    for _ in range(n):
        deck = Deck()
        deck.shuffle()
        hand = Hand(*deck.take(5))
        best_combination = PokerCombination(hand).best_combination().name
        stats[best_combination] = stats.get(best_combination, 0) + 1

    print(f'\nStats after {n} repetitions:')
    for combination in PokerCombinations:
        print(f'{combination.name:40}:{stats.get(combination.name, 0):5}')