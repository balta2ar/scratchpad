#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (33.90%)
# Total Accepted:    358.8K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, remove the n-th node from the end of list and return its
# head.
#
# Example:
#
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes
# 1->2->3->5.
#
#
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?
#
#
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def to_list(python_list):
    tail = head = None

    for val in python_list:
        if head is None:
            tail = head = ListNode(val)
        else:
            tail.next = ListNode(val)
            tail = tail.next

    return head


def from_list(list_node):
    python_list = []

    while list_node:
        python_list.append(list_node.val)
        list_node = list_node.next

    return python_list


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None

        right = head
        for i in range(n):
            right = right.next
        if right is None:
            head = head.next
            return head

        left = head
        while right.next is not None:
            right = right.next
            left = left.next
        left.next = left.next.next
        return head


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    result = Solution().removeNthFromEnd(*input_)
    assert_eq(from_list(result), output)


if __name__ == '__main__':
    assert_eq(from_list(to_list([1, 3, 2, 5])), [1, 3, 2, 5])
    assert_eq(from_list(to_list([])), [])
    assert_eq(from_list(to_list([3])), [3])

    test((to_list([1, 3, 2, 5]), 1), [1, 3, 2])
    test((to_list([1, 3, 2, 5]), 2), [1, 3, 5])
    test((to_list([1, 3, 2, 5]), 3), [1, 2, 5])
    test((to_list([1, 3, 2, 5]), 4), [3, 2, 5])
    test((to_list([]), 4), [])
    test((to_list([1]), 1), [])
    test((to_list([2, 1]), 1), [2])
    test((to_list([2, 1]), 2), [1])
