#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (45.33%)
# Total Accepted:    521.5K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#
#
#
# Definition for singly-linked list.


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def to_list(python_list):
    if python_list is None:
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
        return None
    python_list = []

    while list_node:
        python_list.append(list_node.val)
        list_node = list_node.next

    return python_list


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not (l1 or l2):
            return None
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2

        def append(p, v):
            node = ListNode(v)
            if p is not None:
                p.next = node
            return node

        head = tail = None
        while l1 and l2:
            if l1.val <= l2.val:
                tail = append(tail, l1.val)
                if head is None:
                    head = tail
                l1 = l1.next
            else:
                tail = append(tail, l2.val)
                if head is None:
                    head = tail
                l2 = l2.next
        while l1:
            tail = append(tail, l1.val)
            l1 = l1.next
        while l2:
            tail = append(tail, l2.val)
            l2 = l2.next
        return head


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    l1, l2 = input_
    assert_eq(from_list(Solution().mergeTwoLists(
        to_list(l1), to_list(l2))), output)


if __name__ == '__main__':
    test(([], []), None)
    test((None, None), None)
    test(([], None), None)
    test((None, []), None)

    test(([1], [1]), [1, 1])
    test(([1], [1]), [1, 1])
    test(([1, 2, 2], [1, 1, 2]), [1, 1, 1, 2, 2, 2])
    test(([3, 4, 5], [1, 2]), [1, 2, 3, 4, 5])
    test(([3, 4, 5], [1, 2, 3]), [1, 2, 3, 3, 4, 5])
