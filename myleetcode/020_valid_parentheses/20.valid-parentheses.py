#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (35.68%)
# Total Accepted:    526.8K
# Total Submissions: 1.5M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
# Note that an empty string is also considered valid.
#
# Example 1:
#
#
# Input: "()"
# Output: true
#
#
# Example 2:
#
#
# Input: "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: "(]"
# Output: false
#
#
# Example 4:
#
#
# Input: "([)]"
# Output: false
#
#
# Example 5:
#
#
# Input: "{[]}"
# Output: true
#
#
#


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            if c in '([{':
                stack.append(mapping[c])
            else:
                if not stack:
                    return False
                top = stack.pop()
                if c != top:
                    return False
        return False if stack else True


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().isValid(input_), output)


if __name__ == '__main__':
    test('', True)
    test('{}', True)
    test('[]', True)
    test('[[[]]]', True)
    test('[[[]]', False)
    test('[]]', False)
    test('[{()}]', True)
    test('[()(){([])}]', True)
