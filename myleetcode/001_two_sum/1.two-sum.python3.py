#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (38.21%)
# Total Accepted:    916.8K
# Total Submissions: 2.4M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# Example:
#
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#
#
#
#


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # The idea is simple: use hash to keep track of the seen numbers.
        # Because the `target` is a sum of two numbers, you should be looking
        # for the complementary Y = target - X, where X is the current value.
        seen = {}
        for i, x in enumerate(nums):
            complement = target - x
            if complement in seen:
                return [seen[complement], i]
            seen[x] = i
        return [None, None]
