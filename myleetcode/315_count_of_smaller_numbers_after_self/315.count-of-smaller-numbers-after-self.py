#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (40.94%)
# Total Accepted:    116.4K
# Total Submissions: 284.3K
# Testcase Example:  '[5,2,6,1]'
#
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
#
# Example:
#
#
# Input: [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
#
#
from typing import List


class Solution:
    class SegmentTreeNode:
        def __init__(self, lo, hi):
            self._lo = lo
            self._hi = hi
            self._sum = 0
            self._left = None
            self._right = None
        def increment(self, at, delta):
            if not (self._lo <= at <= self._hi): return
            if self._lo == self._hi == at: self._sum += delta; return
            self._left.increment(at, delta)
            self._right.increment(at, delta)
            self._sum = self._left._sum + self._right._sum
        def sum(self, lo, hi):
            if lo > self._hi or hi < self._lo: return 0
            if lo <= self._lo <= self._hi <= hi: return self._sum
            return self._left.sum(lo, hi) + self._right.sum(lo, hi)

    def _buildSegmentTree(self, lo, hi):
        node = self.SegmentTreeNode(lo, hi)
        if lo == hi: return node
        mid = int((lo + hi) / 2)
        node._left = self._buildSegmentTree(lo, mid)
        node._right = self._buildSegmentTree(mid+1, hi)
        return node

    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums: return []
        # sample input: [5, 2, 6, 1]
        # we build a mapping of integer value to its uniq index:
        # [5, 2, 6, 1] => [1, 2, 5, 6] => {1:0, 2:1, 5:2, 6:3}
        uniq_num_to_index = {v: i for i, v in enumerate(sorted(set(nums)))}
        # we build a segment tree the size of that uniq set
        tree = self._buildSegmentTree(0, len(uniq_num_to_index)-1)
        result = []

        for i in range(len(nums)-1, -1, -1):
            # numbers that are smaller than the current are on the left side
            # of the segment tree representation
            result.append(tree.sum(0, uniq_num_to_index[nums[i]]-1))
            # make number at its offset be seen one more time
            tree.increment(uniq_num_to_index[nums[i]], 1)

        return result[::-1]


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().countSmaller(input_), output)


def test_tree():
    tree = Solution()._buildSegmentTree(0, 3)
    assert_eq(0, tree.sum(0, 3))
    tree.increment(0, 1)
    assert_eq(1, tree.sum(0, 3))
    tree.increment(1, 1)
    assert_eq(2, tree.sum(0, 3))
    assert_eq(1, tree.sum(0, 0))
    assert_eq(1, tree.sum(1, 1))
    assert_eq(0, tree.sum(2, 2))
    assert_eq(0, tree.sum(3, 3))
    tree.increment(2, 1)
    assert_eq(1, tree.sum(2, 2))
    assert_eq(0, tree.sum(3, 3))
    tree.increment(3, 1)
    assert_eq(1, tree.sum(2, 2))
    assert_eq(1, tree.sum(3, 3))
    assert_eq(4, tree.sum(0, 3))


if __name__ == '__main__':
    test_tree()
    test([], [])
    test([1], [0])
    test([5, 2, 6, 1], [2, 1, 1, 0])
