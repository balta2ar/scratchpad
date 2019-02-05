#
# [12] Integer to Roman
#
# https://leetcode.com/problems/integer-to-roman/description/
#
# algorithms
# Medium (46.71%)
# Total Accepted:    147.4K
# Total Submissions: 315.6K
# Testcase Example:  '3'
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M.
#
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, two is written as II in Roman numeral, just two one's added
# together. Twelve is written as, XII, which is simply X + II. The number
# twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There
# are six instances where subtraction is used:
#
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
#
#
# Given an integer, convert it to a roman numeral. Input is guaranteed to be
# within the range from 1 to 3999.
#
# Example 1:
#
#
# Input: 3
# Output: "III"
#
# Example 2:
#
#
# Input: 4
# Output: "IV"
#
# Example 3:
#
#
# Input: 9
# Output: "IX"
#
# Example 4:
#
#
# Input: 58
# Output: "LVIII"
# Explanation: C = 100, L = 50, XXX = 30 and III = 3.
#
#
# Example 5:
#
#
# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
#


# class MyCrudeSolution:
#     def intToRoman(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
#         result = ''
#         while num > 0:
#             if num < 4:
#                 result += 'I'*num
#                 num = 0
#             elif num == 4:
#                 result += 'IV'
#                 num = 0
#             elif 5 <= num < 9:
#                 result += 'V' + 'I'*(num-5)
#                 num = 0
#             elif num == 9:
#                 result += 'IX'
#                 num = 0
#             elif num
#
#         return result


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ['M', 'CM', 'D', 'CD', 'C',
                 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ''

        while num > 0:
            for a, r in zip(arabic, roman):
                if num >= a:
                    result += r
                    num -= a
                    break

        return result


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().intToRoman(input_), output)


if __name__ == '__main__':
    test(3, 'III')
    test(4, 'IV')
    test(9, 'IX')
    test(58, 'LVIII')
    test(59, 'LIX')
    test(1994, 'MCMXCIV')
