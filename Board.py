from CardColumn import CardColumn


class Board:
    def __init__(self, deck):
        self._board = self._generate_board(deck)

    @staticmethod
    def _generate_board(deck):
        b = []
        cnt = 1
        for i in range(9):
            b.append(CardColumn())

        for card in deck:
            b[cnt].append(card)
            cnt += 1
            if cnt == 9:
                cnt = 1

        return b

    def __getitem__(self, item):
        return self._board[item]

    def __str__(self):
        ret = ""

        cnt = [0]
        for i in range(1, 9):
            cnt.append(len(self._board[i])-1)

        complete = False
        while not complete:
            complete = True
            for i in range(1, 9):
                if cnt[i] < 0:
                    ret += '    '
                else:
                    ret += str(self._board[i][cnt[i]])
                    complete = False
                cnt[i] -= 1
            ret += '\n'

        return ret
