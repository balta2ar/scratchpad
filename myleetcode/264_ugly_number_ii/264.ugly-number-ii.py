#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (35.33%)
# Total Accepted:    98.1K
# Total Submissions: 274.9K
# Testcase Example:  '10'
#
# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
#
# Example:
#
#
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
#
# Note:  
#
#
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
#
#
from heapq import heappop, heappush


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1

        counter = 2
        numbers = []
        heappush(numbers, 2)
        heappush(numbers, 3)
        heappush(numbers, 5)
        seen = set([2, 3, 5])

        while True:
            ugly = heappop(numbers)
            if counter == n:
                return ugly
            counter += 1
            for c in (ugly*2, ugly*3, ugly*5):
                if c not in seen:
                    seen.add(c)
                    heappush(numbers, c)


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().nthUglyNumber(input_), output)


if __name__ == '__main__':
    test(1, 1)
    test(2, 2)
    test(3, 3)
    test(4, 4)
    test(5, 5)
    test(10, 12)
