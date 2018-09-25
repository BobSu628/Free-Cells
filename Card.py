class Card:

    char_value = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K']
    char_suit = {'S': chr(9824), 'H': chr(9829), 'C': chr(9827), 'D': chr(9830)}

    def __init__(self, suit, value):
        self._suit = suit
        self._value = value
        self._next = None
        self._color = self._get_color()

    def value(self):
        return self._value

    def suit(self):
        return self._suit

    def set_next(self, next):
        self._next = next

    def next(self):
        return self._next

    def color(self):
        return self._color

    def _get_color(self):
        if self._suit == 'H' or self._suit == 'D':
            return 0
        return 1

    def can_be_stacked_onto_by(self, other):
        if self._color != other.color() and self._value == other.value() + 1:
            return True
        return False

    def __str__(self):
        if self._color == 0:
            return f'\033[1;31m{Card.char_suit[self._suit]}{Card.char_value[self._value]}  \033[0m'

        return f'\033[1;30m{Card.char_suit[self._suit]}{Card.char_value[self._value]}  \033[0m'

    def __repr__(self):
        return f'class Card(suit={self._suit}, value={Card.value[self._value]})'

    def __lt__(self, other):
        if self._value < other.value():
            return True
        return False

    def __gt__(self, other):
        if self._value > other.value():
            return True
        return False

    def __eq__(self, other):
        if self._value == other.value():
            return True
        return False
