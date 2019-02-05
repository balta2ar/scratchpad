#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (40.63%)
# Total Accepted:    327.6K
# Total Submissions: 805.8K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
#
# Example:
#
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
#
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
#
#


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = cur_max = nums[0]
        cur_max = 0

        for i in nums[1:]:
            # either reset the sum by taking the current element (i),
            # or keep growing the sum cur_max + i
            cur_max = max(i, cur_max + i)
            max_so_far = max(max_so_far, cur_max)

        return max_so_far


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().maxSubArray(input_), output)


if __name__ == '__main__':
    test([-2, 1], 1)
    test([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
