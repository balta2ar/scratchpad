#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (42.63%)
# Total Accepted:    288.8K
# Total Submissions: 663.9K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
#
#
#
# Example:
#
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


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


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        return self.reverseKGroup(head, 2)

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        def insert(list_, node):
            if list_ is None:
                return node
            node.next = list_
            return node

        def rev_only_k(head, k):
            if head is None:
                # is that so?
                return True, None, None, None

            nh, nt = None, head
            for i in range(k):
                # early exit, there is no 'next'
                if head is None:
                    return False, nh, nt, None

                next = head.next
                nh = insert(nh, head)
                head = next

            return True, nh, nt, head

        if head is None:
            return None

        ok, nh, nt, next = rev_only_k(head, k)
        if not ok:
            # we've reached the end of the list
            # revert the action and return
            # make sure the tail is a dead end
            nt.next = None
            _ok, nh, nt, _next = rev_only_k(nh, k)
            # make sure the tail is a dead end
            nt.next = None
            return nh

        nh2 = self.reverseKGroup(next, k)
        nt.next = nh2
        return nh


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    list_ = to_list(input_)
    assert_eq(from_list(Solution().swapPairs(list_)), output)


if __name__ == '__main__':
    test([1, 2, 3, 4, 5], [2, 1, 4, 3, 5])
    test([1, 2, 3, 4], [2, 1, 4, 3])
    test([1], [1])
    test([1, 2], [2, 1])
