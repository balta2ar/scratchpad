from typing import List, Optional


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        d = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    d[i][j] = d[i-1][j-1] + 1
                else:
                    d[i][j] = max(d[i-1][j], d[i][j-1])
        return d[n-1][m-1]


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input1, input2, output):
    result = Solution().longestCommonSubsequence(input1, input2)
    assert_eq(result, output)


if __name__ == '__main__':
    test("abcde", "ace", 3)
    test("abc", "abc", 3)
    test("abc", "def", 0)
