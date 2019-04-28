#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (34.57%)
# Total Accepted:    336K
# Total Submissions: 960K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
#
# Note:
#
#
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
#
#
# Example:
#
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]
#
#
#
from typing import List


class Solution:
    def merge(self, a: List[int], m: int, b: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        w = len(a) - 1
        l, r = m-1, n-1

        while l >= 0 and r >= 0:
            if a[l] >= b[r]:
                a[w] = a[l]
                l -= 1
            else:
                a[w] = b[r]
                r -= 1
            w -= 1
        while r >= 0:
            a[w] = b[r]
            r -= 1
            w -= 1
        while l >= 0:
            a[w] = a[l]
            l -= 1
            w -= 1

        # return a


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().merge(*input_), output)


# if __name__ == '__main__':
#     test(([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), [1, 2, 2, 3, 5, 6])
