#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (24.34%)
# Total Accepted:    203.1K
# Total Submissions: 834.6K
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*'.
#
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
#
# The matching should cover the entire input string (not partial).
#
# Note:
#
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# . or *.
#
#
# Example 1:
#
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
#
# Example 2:
#
#
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
#
#
# Example 3:
#
#
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
#
#
# Example 4:
#
#
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore
# it matches "aab".
#
#
# Example 5:
#
#
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false
#
#
#


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Matrix len(s) X len(p)
        # number of rows -- len(s)
        # number of cols -- len(p)
        t = [[False]*(len(p)+1) for _ in range((len(s)+1))]

        # Empty string matches empty pattern
        t[0][0] = True
        for i in range(1, len(p)+1):
            # Match for X* is the same with the match for the letters before it
            if p[i-1] == '*':
                t[0][i] = t[0][i-2]

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                # If previous letters were equal or previous pattern was '.'
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    # Take match from that previous pair
                    t[i][j] = t[i-1][j-1]
                elif p[j-1] == '*':
                    # Presume we haven't seen X*
                    t[i][j] = t[i][j-2]  # 0 occurences of X*
                    # Similar to the first if, but now check previous pair
                    # of text, pattern as current p[j] is '*'
                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        t[i][j] = t[i][j] or t[i-1][j]
                else:
                    t[i][j] = False

        return t[len(s)][len(p)]


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().isMatch(*input_), output)


if __name__ == '__main__':
    test(('aa', 'a'), False)
    test(('aa', 'a*'), True)
    test(('ab', '.*'), True)
    test(('aab', 'c*a*b'), True)
    test(('mississippi', 'mis*is*p*.'), False)
