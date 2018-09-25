class CardColumn:
    def __init__(self):
        self._head = None
        self._length = 0

    def head(self):
        return self._head

    def tail(self):
        return self._tail

    def length(self):
        return self._length

    def is_empty(self):
        if self._length == 0:
            return True

        return False

    def append(self, card):
        if self._head is None:
            self._head = card
        else:
            card.set_next(self._head)
            self._head = card
        self._length += 1

    def append_stack(self, head):
        if self._head is None:
            self._head = head
        else:
            stack = [head]
            cur = head
            length = 1
            while cur.next() is not None:
                cur = cur.next()
                stack.append(cur)
                length += 1

            i = len(stack) - 1
            while i >= 0:
                self.append(stack[i])
                i -= 1

    def pop(self):
        tmp = self._head
        self._head = self._head.next()
        tmp.set_next(None)
        self._length -= 1

        return tmp

    def pop_stack(self, length):
        first = self._head
        for _ in range(length-1):
            self._head = self._head.next()

        last = self._head
        self._head = self._head.next()
        last.set_next(None)
        self._length -= length

        return first

    def can_be_stacked_onto_by(self, card):
        if self._head.can_be_stacked_onto_by(card):
            return True

        return False

    def stack_is_valid(self, length):
        if length <= 0 or length > self._length:
            return False
        cur = self._head
        for _ in range(length-1):
            nxt = cur.next()
            if not nxt.can_be_stacked_onto_by(cur):
                return False

        return True

    def __getitem__(self, item):
        ret = self._head
        for _ in range(item):
            ret = ret.next()

        return ret

    def __len__(self):
        return self._length
