from Card import Card
import random


class Deck:

    suits = ['S', 'H', 'C', 'D']

    def __init__(self):
        self._deck = self._generate_deck()
        self._index = -1

    def _generate_deck(self):
        d = []

        for s in Deck.suits:
            for v in range(1, 14):
                d.append(Card(s, v))

        random.shuffle(d)
        return d

    def deck(self):
        return self._deck

    def __next__(self):
        self._index += 1
        if self._index < len(self._deck):
            return self._deck[self._index]
        else:
            raise StopIteration

    def __iter__(self):
        self._index = -1
        return self
