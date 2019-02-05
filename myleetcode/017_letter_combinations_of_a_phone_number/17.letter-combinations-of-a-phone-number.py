#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (39.96%)
# Total Accepted:    335.1K
# Total Submissions: 838.5K
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
#
#
#
# Example:
#
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
# Note:
#
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
#
#
from typing import List


MAPPING = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = []

        def helper(digits_remains: str, path: str):
            if not digits_remains:
                result.append(path)
                return

            for char in MAPPING[digits_remains[0]]:
                helper(digits_remains[1:], path + char)

        helper(digits, path='')
        return result


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().letterCombinations(input_), output)


if __name__ == '__main__':
    test("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
