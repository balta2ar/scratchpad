#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (24.38%)
# Total Accepted:    419.3K
# Total Submissions: 1.7M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
#
# Input: 123
# Output: 321
#
#
# Example 2:
#
#
# Input: -123
# Output: -321
#
#
# Example 3:
#
#
# Input: 120
# Output: 21
#
#
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
# this problem, assume that your function returns 0 when the reversed integer
# overflows.
#
#


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        # Simply divide the integer and add it to the result, multiplying
        # by 10 on each step.
        y = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        while x > 0:
            y += x % 10
            x = x // 10
            if x > 0:
                y *= 10

        y = y * sign

        if not -(2 ** 31) <= y <= (2 ** 31)-1:
            return 0

        return y


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().reverse(input_), output)


if __name__ == '__main__':
    test(123, 321)
    test(-123, -321)
    test(120, 21)
    test(1534236469, 0)
