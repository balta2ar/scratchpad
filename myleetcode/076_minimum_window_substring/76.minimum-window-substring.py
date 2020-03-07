#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (29.57%)
# Total Accepted:    228.3K
# Total Submissions: 749K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
#
# Example:
#
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
#
#
# Note:
#
#
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.
#
#
from collections import Counter, namedtuple

Subarray = namedtuple('Subarray', 'start end')


class Solution:
    def minWindow(self, items: str, keywords: str) -> str:
        keywords_to_cover = Counter(keywords)
        remains_to_cover = len(keywords)
        result = Subarray(-1, -1)

        left = 0
        for right, rword in enumerate(items):
            # The right boundary has expanded, and so has the cover set
            if rword in keywords_to_cover:
                keywords_to_cover[rword] -= 1
                if keywords_to_cover[rword] >= 0:
                    remains_to_cover -= 1

            # Try to shrink (move) left boundary while possible
            while remains_to_cover == 0:
                if (result.start == -1) or (right - left < result.end - result.start):
                    result = Subarray(left, right)

                lword = items[left]
                if lword in keywords_to_cover:
                    keywords_to_cover[lword] += 1
                    if keywords_to_cover[lword] > 0:
                        remains_to_cover += 1
                left += 1

        return items[result.start: result.end + 1]


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def append(self, value):
        node = Node(value)
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        self.size += 1

    def remove(self, node):
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        node.next = node.prev = None
        self.size -= 1


class SolutionKeywordsMustBeUnique:
    def minWindow(self, items: str, keywords: str) -> str:
        seen = DoubleLinkedList()
        word_to_node = {keyword: None for keyword in keywords}
        result = Subarray(-1, -1)

        for index, item in enumerate(items):
            # Not a keyword, skip it
            if item not in word_to_node:
                continue

            node = word_to_node[item]
            if node is not None:
                seen.remove(node)
            seen.append(index)
            word_to_node[item] = seen.tail

            if len(seen) == len(keywords):
                if (result.start == -1) or (index - seen.head.data < result.end - result.start):
                    print('update', seen.head.data, index)
                    result = Subarray(seen.head.data, index)

        return items[result.start: result.end + 1]


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    s, t = input_
    assert_eq(Solution().minWindow(s, t), output)


if __name__ == '__main__':
    test(('ADOBECODEBANC', 'ABC'), 'BANC')
    test(('aa', 'aa'), 'aa')
