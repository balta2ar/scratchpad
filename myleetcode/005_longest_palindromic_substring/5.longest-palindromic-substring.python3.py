#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (25.43%)
# Total Accepted:    322.8K
# Total Submissions: 1.3M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
#
# Example 1:
#
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: "cbbd"
# Output: "bb"
#
#
#


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s

        def largest(i, j, start_size, best):
            start, size = i, start_size
            cur = s[start:start+size]
            while i >= 0 and j < len(s) and s[i] == s[j]:
                start = i
                size = j - i + 1
                i -= 1
                j += 1
            cur = s[start:start+size]
            return cur if len(cur) > len(best) else best

        # The algorithm tries every i in the string, and expand a palindrom
        # from that point while it's possible, remembers largest value.
        # Complexity O(n^2).
        best = s[0:1]
        for i in range(0, len(s) - 1):
            best = largest(i, i, 1, best)
            best = largest(i, i+1, 0, best)
        return best


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().longestPalindrome(input_), output)


if __name__ == '__main__':
    test('cbbd', 'bb')
    test('babad', 'bab')
