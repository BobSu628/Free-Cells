class FreeCells:
    def __init__(self):
        self._len = 0
        self._cells = [None, None, None, None]

    def len(self):
        return self._len

    def cells(self):
        return self._cells

    def append(self, card):
        self._cells[self._len] = card
        self._len += 1

    def cells_full(self):
        if self._len >= 4:
            return True

        return False

    def remove(self, index):
        ret = self._cells.pop(index-1)
        self._len -= 1
        self._cells.append(None)
        return ret

    def index_illegal(self, index):
        if index < 1 or index > self._len:
            return True

        return False

    def __getitem__(self, item):
        return self._cells[item-1]

    def __str__(self):
        ret = ""
        for card in self._cells:
            if card is None:
                ret += "__  "
            else:
                ret += str(card)

        ret += "        "
        return ret
