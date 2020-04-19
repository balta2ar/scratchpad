#
# @lc app=leetcode id=327 lang=python3
#
# [327] Count of Range Sum
#
# https://leetcode.com/problems/count-of-range-sum/description/
#
# algorithms
# Hard (34.52%)
# Total Accepted:    40K
# Total Submissions: 115.5K
# Testcase Example:  '[-2,5,-1]\n-2\n2'
#
# Given an integer array nums, return the number of range sums that lie in
# [lower, upper] inclusive.
# Range sum S(i, j) is defined as the sum of the elements in nums between
# indices i and j (i ≤ j), inclusive.
#
# Note:
# A naive algorithm of O(n^2) is trivial. You MUST do better than that.
#
# Example:
#
#
# Input: nums = [-2,5,-1], lower = -2, upper = 2,
# Output: 3
# Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective
# sums are: -2, -1, 2.
#
#
from typing import List


class Solution:
    # brute force
    def countRangeSumBruteForce(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        sumK = [0] * (n+1)
        for i in range(1, n+1):
            sumK[i] = sumK[i-1] + nums[i-1]

        count = 0
        for j in range(n+1):
            for i in range(j):
                #sumRange = sumK[j] - sumK[i]
                if lower <= sumK[j] - sumK[i] <= upper: count += 1

        print(sumK)
        return count

    class SegmentTreeNode:
        def __init__(self, min_, max_):
            self.min_ = min_
            self.max_ = max_
            self.count = 0
            self.left = None
            self.right = None
        def update(self, value):
            if self.min_ <= value <= self.max_:
                self.count += 1
                # print('new count', self.count, 'min max', self.min_, self.max_)
                if self.left: self.left.update(value)
                if self.right: self.right.update(value)
        def get_count(self, min_, max_):
            if self.max_ < min_ or self.min_ > max_: return 0
            if min_ <= self.min_ <= self.max_ <= max_: return self.count
            count = 0
            # print('counting', min_, max_, count)
            count += self.left.get_count(min_, max_) if self.left else 0
            count += self.right.get_count(min_, max_) if self.right else 0
            return count

    def build(self, values, lo, hi):
        if lo > hi: return None
        node = self.SegmentTreeNode(values[lo], values[hi])
        if lo == hi: return node
        mid = int((lo + hi) / 2)
        node.left = self.build(values, lo, mid)
        node.right = self.build(values, mid+1, hi)
        return node

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        if not nums or len(nums) == 0: return 0
        if len(nums) == 1: return int(lower <= nums[0] <= upper)
        from itertools import accumulate
        # This array represents prefix sum, referred to later as sum_j
        # In brute-force solution we do:
        #     if lower <= sumK[j] - sumK[i] <= upper: count += 1
        # Here we prepare/precompute the sumK[j] part of the expression
        uniqPrefixSum = sorted(set([0] + list(accumulate(nums))))
        # print('--- nums', nums, 'prefix', uniqPrefixSum)
        node = self.build(uniqPrefixSum, 0, len(uniqPrefixSum)-1)
        count, sum_ = 0, 0 #int(lower <= nums[0] <= upper), nums[0]
        for i in range(0, len(nums)):
            node.update(sum_)
            sum_ += nums[i]
            # print('old sum', sum_-nums[i], 'new sum', sum_)
            # count += int(lower <= sum_ <= upper)

            # We need to walk through our prefix sums (sum_j) and find how many
            # satify the equation:
            #     lower <= sum_j - sum_i <= higher
            # OR
            #     lower <= currentPrefixSum - previousPrefixSum <= higher
            #
            # previousPrefixSum is added here before sum_ is updated: node.update(sum_)
            #
            # Rewriting the expression above:
            #     lower <= currentPrefixSum - previousPrefixSum <= higher
            #     lower - currentPrefixSum <= - previousPrefixSum <= higher - currentPrefixSum
            #     currentPrefixSum - lower => previousPrefixSum => currentPrefixSum - higher
            #     currentPrefixSum - higher <= previousPrefixSum <= currentPrefixSum - lower
            #
            # At this line currentPrefixSum = sum_, so we get:
            count += node.get_count(sum_-upper, sum_-lower)
        return count


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, lo, hi, output):
    assert_eq(Solution().countRangeSum(input_, lo, hi), output)


if __name__ == '__main__':
    test([-1, 1], 0, 0, 1)
    test([-2, 5, -1], -2, 2, 3)
