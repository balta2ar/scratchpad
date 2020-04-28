from typing import List, Optional


class FirstUnique:

    class DoubleExtendedList:
        class Item:
            def __init__(self, value, count):
                self.value = value
                self.count = count
                self._next = None
                self._prev = None

        def __init__(self):
            self._head = None
            self._tail = None
            self._size = 0
        def __len__(self): return self._size
        def head(self): return self._head.value if self._head else -1
        def tail(self): return self._tail.value if self._tail else -1
        def append_tail(self, value):
            node = self.Item(value, 1)
            node._next = None
            node._prev = self._tail
            if self._tail: self._tail._next = node; self._tail = node
            else: self._tail = self._head = node
            return node
        def append_head(self, value):
            node = self.Item(value, 1)
            node._next = self._head
            node._prev = None
            if self._head: self._head._prev = node; self._head = node
            else: self._head = self._tail = node
            return node
        def remove(self, node):
            assert node, 'cannot remove None from a list'
            if self._head == self._tail == node:
                self._head = self._tail = None
                return
            next_ = node._next
            prev = node._prev
            if next_: next_._prev = prev
            if prev: prev._next = next_
            if self._head == node: self._head = next_
            if self._tail == node: self._tail = prev

    def __init__(self, nums: List[int]):
        self._map = dict()
        self._list = self.DoubleExtendedList()
        for x in nums:
            self.add(x)

    def showFirstUnique(self) -> int:
        return self._list.head()

    def add(self, value: int) -> None:
        if value in self._map:
            node = self._map[value]
            if node.count == 1:
                self._list.remove(node)
            node.count += 1
            return

        node = self._list.append_tail(value)
        self._map[value] = node


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


# def test(input1, output):
#     result = Solution().maximalSquare(input1)
#     assert_eq(result, output)


if __name__ == '__main__':
    dlist = FirstUnique.DoubleExtendedList()
    assert_eq(dlist.head(), -1)
    assert_eq(dlist.tail(), -1)
    node5 = dlist.append_head(5)
    assert_eq(dlist.head(), 5)
    assert_eq(dlist.tail(), 5)
    node1 = dlist.append_head(1)
    assert_eq(dlist.head(), 1)
    assert_eq(dlist.tail(), 5)
    node10 = dlist.append_tail(10)
    assert_eq(dlist.head(), 1)
    assert_eq(dlist.tail(), 10)
    dlist.remove(node5)
    assert_eq(dlist.head(), 1)
    assert_eq(dlist.tail(), 10)
    dlist.remove(node1)
    assert_eq(dlist.head(), 10)
    assert_eq(dlist.tail(), 10)
    dlist.remove(node10)
    assert_eq(dlist.head(), -1)
    assert_eq(dlist.tail(), -1)

    uniq = FirstUnique([2, 3, 5])
    assert_eq(uniq.showFirstUnique(), 2)
    uniq.add(5)
    assert_eq(uniq.showFirstUnique(), 2)
    uniq.add(2)
    assert_eq(uniq.showFirstUnique(), 3)
    uniq.add(3)
    assert_eq(uniq.showFirstUnique(), -1)

    uniq = FirstUnique([7,7,7,7,7,7])
    assert_eq(uniq.showFirstUnique(), -1)
    uniq.add(7)
    uniq.add(3)
    uniq.add(3)
    uniq.add(7)
    uniq.add(17)
    assert_eq(uniq.showFirstUnique(), 17)

    uniq = FirstUnique([809])
    assert_eq(uniq.showFirstUnique(), 809)
    uniq.add(809)
    assert_eq(uniq.showFirstUnique(), -1)
