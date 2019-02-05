#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (23.08%)
# Total Accepted:    465.3K
# Total Submissions: 2M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
#
from typing import List


class MyWrongNaiveSolution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()
        print(nums)

        complements = dict()
        for ia, a in enumerate(nums):
            for ib, b in enumerate(nums[ia+1:]):
                complement = 0 - a - b
                if complement in complements:
                    ic = complements[complement]
                    if ia != ib and ia != ic:
                        results.add(tuple(sorted((a, b, complement))))
                else:
                    complements[a] = ia
                    complements[b] = ib

        return sorted(list(results))


# Since the list nums is sorted and we go from negative to positive, the first
# time we compute -v-x in the if condition will result in the high value in
# (low, mid, high) tuple. negative of a negative is positive (left to right!).
# the second time we encounter x, which has been added to the dictionary d, x
# would be the high value we computed previously in our first encounter, see
# above. Thus, -v-x this time will be the mid value. That's it. low is fixed in
# the first for loop. high is computed from left to right and stored in
# dictionary. mid is computed based on low and high => (low, mid, high).


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        results = set()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            complements = set()
            for j, b in enumerate(nums[i+1:]):
                if b in complements:
                    # If b was added to complements, it means that
                    # 1. we've seen a (a, ?, ?)
                    # 2. this number is third in the triplet (a, ?, b)
                    # 3. we have seen "-a-b" and added before in this loop
                    results.add((a, -a-b, b))
                else:
                    # if b is something new, then it means that:
                    # 1. we've seen a
                    # 2. this is the first occurence of b, it means it's the
                    #    second number in a triplet (?, b, ?)
                    # 3. we remember the missing third number: 0-a-b
                    complements.add(-a-b)

        return sorted(list(map(list, results)))


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().threeSum(input_), output)


if __name__ == '__main__':
    test([-1, 0, 1, 2, -1, -4],
         sorted(map(list, [(-1, 0, 1), (-1, -1, 2)])))
