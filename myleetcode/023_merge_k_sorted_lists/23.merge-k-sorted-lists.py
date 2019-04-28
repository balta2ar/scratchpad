#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (32.43%)
# Total Accepted:    350.7K
# Total Submissions: 1.1M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
#
# Example:
#
#
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
#
#
#
# Definition for singly-linked list.
from heapq import heappop, heappush
from typing import List


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


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
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = tail = None

        def append(p, v):
            node = ListNode(v)
            if p is not None:
                p.next = node
            return node

        queue = []
        # storage = {}
        for index, list_ in enumerate(lists):
            if list_:
                # storage[id(list_)] = list_
                # Instead of a storage we use a tiebreaker here: some number
                # that is unique for each list. This is to make sure that
                # ListNode is never compared to each other -- so that we don't
                # have to implement "<" operation over them.
                heappush(queue, (list_.val, index, list_))

        while queue:
            val, index, p = heappop(queue)
            # p = storage[p]
            tail = append(tail, val)
            if head is None:
                head = tail

            if p.next:
                # storage[id(p.next)] = p.next
                heappush(queue, (p.next.val, index, p.next))

        return head


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    input_ = [to_list(x) for x in input_]
    result = from_list(Solution().mergeKLists(input_))
    assert_eq(result, output)


if __name__ == '__main__':
    test(
        [[]],
        []
    )
    test(
        [[], []],
        []
    )
    test(
        [[1], [1, 2], []],
        [1, 1, 2]
    )
    test(
        [[], [], [3, 4], [1, 5]],
        [1, 3, 4, 5]
    )
    test(
        [[1, 4, 5], [1, 3, 4], [2, 6]],
        [1, 1, 2, 3, 4, 4, 5, 6]
    )
