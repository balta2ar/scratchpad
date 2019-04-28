#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (22.95%)
# Total Accepted:    125.2K
# Total Submissions: 538.4K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string, s, and a list of words, words, that are all of the
# same length. Find all starting indices of substring(s) in s that is a
# concatenation of each word in words exactly once and without any intervening
# characters.
#
# Example 1:
#
#
# Input:
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar"
# respectively.
# The output order does not matter, returning [9,0] is fine too.
#
#
# Example 2:
#
#
# Input:
# ⁠ s = "wordgoodgoodgoodbestword",
# ⁠ words = ["word","good","best","word"]
# Output: []
#
#
#
from typing import List
from collections import Counter, defaultdict


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        counts = Counter(words)
        N = len(s)
        word_len = len(words[0])
        num_words = len(words)

        indices = []
        for i in range(0, N - num_words * word_len + 1):
            seen = defaultdict(int)

            for j, w in enumerate(words):
                word = s[i + j*word_len: i + (j+1) * word_len]
                if word not in counts:
                    break

                seen[word] += 1
                if seen[word] > counts[word]:
                    break
            else:
                indices.append(i)

        return indices


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    s, words = input_
    assert_eq(sorted(Solution().findSubstring(s, words)), sorted(output))


if __name__ == '__main__':
    test(('barfoothefoobarman', ['foo', 'bar']), [0, 9])
    test(('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'word']), [])
    test(('foobaryay', ['bar', 'yay']), [3])
    test(('foobaryay', ['bar', 'yay', 'nop']), [])
