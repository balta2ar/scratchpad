#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (40.27%)
# Total Accepted:    175.9K
# Total Submissions: 422.9K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
#
# Example 2:
#
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#
from bisect import bisect_right
from itertools import count, takewhile


class SolutionRecursive:
    def numSquares(self, n: int) -> int:
        squares = list(takewhile(lambda x: x <= n, (x*x for x in count(1))))

        def find_le(a, x):
            i = bisect_right(a, x)
            if i:
                return i
            raise ValueError()

        def helper(n, depth):
            if n < 0:
                return None
            if n == 0:
                return depth

            best_depth = None
            limit_index = find_le(squares, n)
            for i in range(limit_index-1, -1, -1):
                new_n = n - squares[i]
                new_depth = helper(new_n, depth+1)
                if new_depth is not None:
                    if best_depth is None or new_depth < best_depth:
                        best_depth = new_depth
            return best_depth

        return helper(n, 0)


class SolutionDP:
    def numSquares(self, n: int) -> int:
        dp = [float('+inf')]*(n+1)
        dp[0] = 0

        for i in range(n+1):
            j = 0
            while j*j <= i:
                dp[i] = min(dp[i], dp[i-j*j] + 1)
                j += 1

        return dp[n]


class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n

        squares = list(takewhile(lambda x: x <= n, (x*x for x in count(1))))
        level = 0
        front = {n}
        while front:
            level += 1
            temp = set()
            for x in front:
                for s in squares:
                    if s == x:
                        return level
                    if x < s:
                        break
                    temp.add(x-s)
            front = temp

        return level


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().numSquares(input_), output)


if __name__ == '__main__':
    test(12, 3)
    test(13, 2)
    test(40, 2)
