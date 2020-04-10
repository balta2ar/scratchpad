#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#
# https://leetcode.com/problems/range-sum-query-mutable/description/
#
# algorithms
# Medium (32.73%)
# Total Accepted:    96.6K
# Total Submissions: 295.2K
# Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
#
# The update(i, val) function modifies nums by updating the element at index i
# to val.
#
# Example:
#
#
# Given nums = [1, 3, 5]
#
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
#
#
# Note:
#
#
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is
# distributed evenly.
#
#
#

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        # use 2*N if you use Euler tour order traversal later (pre-order)
        # use 4*N if you use classic 2*node, 2*node+1
        self.tree = [0] * 2 * len(nums)  # 4?
        if len(nums):
            self._build(1, 0, len(nums)-1)

    def _build(self, node, start, end):
        if (start == end):
            self.tree[node] = self.nums[start]
        else:
            mid = int((start + end) / 2)
            # Euler tour order traversal (pre-order)
            lnode, rnode = node+1, node + 2*(mid-start+1)
            self._build(lnode, start, mid)
            self._build(rnode, mid+1, end)
            self.tree[node] = self.tree[lnode] + self.tree[rnode]

    def update(self, i: int, val: int) -> None:
        self._update(1, 0, len(self.nums)-1, i, val - self.nums[i])

    def _update(self, node, start, end, idx, val):
        if start == end:
            self.nums[idx] += val
            self.tree[node] += val
        else:
            mid = int((start + end) / 2)
            lnode, rnode = node+1, node + 2*(mid-start+1)
            if start <= idx <= mid:
                self._update(lnode, start, mid, idx, val)
            else:
                self._update(rnode, mid+1, end, idx, val)
            self.tree[node] = self.tree[lnode] + self.tree[rnode]

    def sumRange(self, i: int, j: int) -> int:
        return self._query(1, 0, len(self.nums)-1, i, j)

    def _query(self, node, start, end, l, r):
        if r < start or l > end:
            return 0
        elif l <= start and end <= r:
            return self.tree[node]

        mid = int((start + end) / 2)
        lnode, rnode = node+1, node + 2*(mid-start+1)
        p1 = self._query(lnode, start, mid, l, r)
        p2 = self._query(rnode, mid+1, end, l, r)
        return p1 + p2


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, updates, sums):
    obj = NumArray(input_)
    for (at, val) in updates:
        obj.update(at, val)
    for (fromm, to, val) in sums:
        result = obj.sumRange(fromm, to)
        assert_eq(result, val)


if __name__ == '__main__':
    test([], [], [])
    test([-28, -39, 53, 65, 11, -56, -65, -39, -43, 97], [], [])

    test([1, 2, 3], [], [(0, 2, 6)])
    test([1, 2, 3], [], [(0, 0, 1)])
    test([1, 2, 3], [], [(1, 1, 2)])
    test([1, 2, 3], [], [(2, 2, 3)])
    test([1, 2, 3], [], [(0, 1, 3)])
    test([1, 2, 3], [], [(1, 2, 5)])

    # test([1, 2, 3], [(1, -2)], [(0, 2, 4)])
    # test([1, 2, 3], [(0, -1), (1, -2), (2, -3)], [(0, 2, 0)])

    test([1, 2, 3], [(1, 0)], [(0, 2, 4)])
    test([1, 2, 3], [(0, 0), (1, 0), (2, 0)], [(0, 2, 0)])
