from typing import List
from collections import namedtuple


class MinStack:
    Item = namedtuple('Item', 'value minsofar')

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.elements = []

    def push(self, x: int) -> None:
        minsofar = min(x, self.elements[-1].minsofar) if self.elements else x
        item = self.Item(x, minsofar)
        self.elements.append(item)

    def pop(self) -> None:
        self.elements.pop()

    def top(self) -> int:
        return self.elements[-1].value

    def getMin(self) -> int:
        return self.elements[-1].minsofar


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(inputS, inputT, output):
    assert_eq(Solution().backspaceCompare(inputS, inputT), output)


if __name__ == '__main__':
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    assert_eq(-3, stack.getMin())
    stack.pop()
    assert_eq(0, stack.top())
    assert_eq(-2, stack.getMin())
