#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (29.41%)
# Total Accepted:    206.1K
# Total Submissions: 700.6K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.
#
# Example:
#
#
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
#
#
#
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums.sort()
        result = set()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            for j in range(i+1, len(nums)):
                b = nums[j]

                seen = set()
                for c in nums[j+1:]:
                    if c in seen:
                        result.add((a, b, target-a-b-c, c))
                    else:
                        seen.add(target-a-b-c)

        return list(map(list, result))


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(sorted(Solution().fourSum(*input_)), sorted(output))


if __name__ == '__main__':
    test(([1, 0, -1, 0, -2, 2], 0),
         [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]])

    test(([-1, 0, 1, 2, -1, -4], -1),
         [[-4, 0, 1, 2], [-1, -1, 0, 1]])
