from Card import Card


class DiscardCells:
    value = ['_', 'A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K']
    suit_index = {'S': 0, 'H': 1, 'C': 2, 'D': 3}

    def __init__(self):
        self._cells = [Card('S', 0), Card('H', 0), Card('C', 0), Card('D', 0)]

    def cells(self):
        return self._cells

    def append(self, card):
        index = DiscardCells.suit_index[card.suit()]
        self._cells[index] = card

    def can_be_discarded(self, card):
        index = DiscardCells.suit_index[card.suit()]
        if card.value() == self._cells[index].value() + 1:
            return True

        return False

    def win(self):
        for card in self._cells:
            if card.value() != 13:
                return False

        return True

    def __str__(self):
        ret = ""
        for card in self._cells:
            if card.value() == 0:
                ret += "__  "
            else:
                ret += str(card)

        ret += '\n\n'
        return ret
