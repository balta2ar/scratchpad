#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (34.98%)
# Total Accepted:    171.1K
# Total Submissions: 481.4K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in
# the end should remain as it is.
#
#
#
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
#
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be
# changed.
#
#
#
# Definition for singly-linked list.


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
    list_, k = input_
    list_ = to_list(list_)
    assert_eq(from_list(Solution().reverseKGroup(list_, k)), output)


if __name__ == '__main__':
    test(([1, 2, 3, 4, 5], 2), [2, 1, 4, 3, 5])
    test(([1, 2, 3, 4, 5, 6], 2), [2, 1, 4, 3, 6, 5])
    test(([1, 2, 3, 4, 5], 3), [3, 2, 1, 4, 5])
    test(([1, 2, 3, 4, 5], 1), [1, 2, 3, 4, 5])
    test(([1, 2, 3, 4, 5], 4), [4, 3, 2, 1, 5])
    test(([1, 2, 3, 4, 5], 5), [5, 4, 3, 2, 1])
