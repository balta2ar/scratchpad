#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (36.59%)
# Total Accepted:    341.2K
# Total Submissions: 932.5K
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
#
# Example 1:
#
#
# Input: 121
# Output: true
#
#
# Example 2:
#
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
#
#
# Example 3:
#
#
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#
# Follow up:
#
# Coud you solve it without converting the integer to a string?
#
#


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Easy way
        # return str(x) == str(x)[::-1]

        if x < 0:
            return False

        # Without converting to a string
        y, temp = 0, x
        while temp > 0:
            y = y * 10 + temp % 10
            temp = temp // 10

        # Another idea is to divide only half of the number

        return x == y


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().isPalindrome(input_), output)


if __name__ == '__main__':
    test(121, True)
    test(-121, False)
    test(10, False)
