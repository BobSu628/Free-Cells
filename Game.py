from Deck import Deck
from Board import Board
from CardColumn import CardColumn
from FreeCells import FreeCells
from DiscardCells import DiscardCells


class Game:

    suits = ['S', 'H', 'C', 'D']
    suit_index = {'S': 0, 'H': 1, 'C': 2, 'D': 3}

    def __init__(self):
        self._deck = Deck()
        self._board = Board(self._deck)
        self._free_cells = FreeCells()
        self._discard_cells = DiscardCells()

    def deck(self):
        return self._deck

    def board(self):
        return self._board

    def free_cells(self):
        return self._free_cells

    def discard_cells(self):
        return self._discard_cells

    def win(self):
        return self._discard_cells.win()

    def free(self, index):
        if self._board[index].is_empty():
            print("This column is empty")
            return

        if self._free_cells.cells_full():
            print("The free cells are full")
            return

        self._free_cells.append(self._board[index].pop())

    def discard(self, index):
        if self._board[index].is_empty():
            print("This column is empty")
            return

        if not self._discard_cells.can_be_discarded(self._board[index].head()):
            print("This card cannot be discarded at this point")
            return

        self._discard_cells.append(self._board[index].pop())

    def retrieve(self, start, end):
        if not self._board[end].can_be_stacked_onto_by(self._free_cells[start]):
            print("Illegal movement of card")
            return

        self._board[end].append(self._free_cells.remove(start))

    def move(self, start, end, qty=1):
        if not self._board[start].stack_is_valid(qty):
            print("Cards to be moved do not form a stack")
            return

        last_card = self._board[start].pop_stack(qty)
        if not self._board[end].can_be_stacked_onto_by(last_card):
            print("Illegal movement of card")
            self._board[start].append(last_card)
            return

        self._board[end].append(last_card)

    def __str__(self):
        return str(self._free_cells) + str(self._discard_cells) + str(self._board)
