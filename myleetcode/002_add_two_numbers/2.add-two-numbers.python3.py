#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (28.76%)
# Total Accepted:    499K
# Total Submissions: 1.7M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
#
#
# Definition for singly-linked list.


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # This is pretty staightforward: just keep summing items of the list
        # and keep in mind two things:
        # 1. don't forget the carry bit
        # 2. if one of the lists is over, just use zeros instead.
        # 3. in the end add carry bit if present
        carry = 0
        head, tail = None, None
        current_l1, current_l2 = l1, l2

        while current_l1 or current_l2:
            val_l1 = current_l1.val if current_l1 else 0
            val_l2 = current_l2.val if current_l2 else 0
            S = val_l1 + val_l2 + carry
            carry, S = 1 if S // 10 > 0 else 0, S % 10
            tail = self.append(tail, S)
            head = head if head else tail
            current_l1 = current_l1.next if current_l1 else None
            current_l2 = current_l2.next if current_l2 else None

        if carry:
            self.append(tail, carry)
        return head

    def append(self, l, val):
        item = ListNode(val)
        if l:
            l.next = item
        return item
