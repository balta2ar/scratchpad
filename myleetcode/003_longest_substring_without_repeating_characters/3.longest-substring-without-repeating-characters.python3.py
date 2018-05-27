#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (24.76%)
# Total Accepted:    491.9K
# Total Submissions: 2M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the
# answer must be a substring, "pwke" is a subsequence and not a substring.
#


class SolutionBruteForce:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        # Not exactly brute force, but its complexity is O(n^2). Iterate over
        # the string and try to find the longest sequence of unique items
        # keeping track of seen items in a set. Then restart with the following
        # character.

        for i, v in enumerate(s):
            seen = set()
            cur_max_len = 0

            for j, w in enumerate(s[i:]):
                if w in seen:
                    break
                cur_max_len += 1
                seen.add(w)

            max_len = max(max_len, cur_max_len)

        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # This one's more efficient, O(2n). Use a sliding window of seen
        # characters. As you encounter a character in the right, check if it's
        # new, add it to `seen`. It's already seen, keep removing characters
        # from the lest side, adjust it, until sliding window shrinks to the
        # set of unique characters.
        i, j, n = 0, 0, len(s)
        max_len = 0
        seen = set()

        while i < n and j < n:
            if s[j] in seen:
                if s[i] in seen:
                    seen.remove(s[i])
                i += 1
            else:
                seen.add(s[j])
                j += 1
                max_len = max(max_len, j - i)

        return max_len


# if __name__ == '__main__':
#     import sys
#     print(Solution().lengthOfLongestSubstring(sys.argv[1]))
