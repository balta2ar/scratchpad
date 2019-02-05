#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (33.82%)
# Total Accepted:    232.9K
# Total Submissions: 688.6K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
#
# Example:
#
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
#
#
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return []

        nums.sort()
        closest = sum(nums[:3])

        a = 0
        while a < len(nums) - 2:
            if a > 0 and nums[a] == nums[a-1]:
                a += 1
                continue

            b, c = a + 1, len(nums) - 1
            while b < c:
                current_sum = nums[a] + nums[b] + nums[c]
                if current_sum == target:
                    return current_sum
                # are we any better now compared to the best previous result?
                if abs(target-current_sum) < abs(target-closest):
                    closest = current_sum
                if current_sum > target:
                    # the sum is too large. since we have sorted the input,
                    # the only way to decrease the sum is to move the right
                    # pointer to the left
                    c -= 1
                else:
                    # similarly, since input is sorted, move left pointer to
                    # the right to make the sum bigger
                    b += 1
            a += 1

        return closest


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().threeSumClosest(*input_), output)


if __name__ == '__main__':
    test(([-1, 2, 1, -4], 1), 2)
