from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def to_list(python_list):
    if not python_list:
        return None
    tail = head = None

    for val in python_list:
        if head is None:
            tail = head = ListNode(val)
        else:
            tail.next = ListNode(val)
            tail = tail.next

    return head


def from_list(list_node):
    if list_node is None:
        return []
    python_list = []

    while list_node:
        python_list.append(list_node.val)
        list_node = list_node.next

    return python_list


def insert(list_, node):
    if list_ is None:
        return node
    node.next = list_
    return node


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        double = head
        single = head

        while double and double.next:
            single = single.next
            double = double.next.next

        return single


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().middleNode(to_list(input_)).val, output)


if __name__ == '__main__':
    test([1, 2, 3, 4, 5], 3)
    test([1, 2, 3, 4, 5, 6], 4)
    test([1], 1)
    test([1, 2], 2)
    test([1, 2, 3], 2)
