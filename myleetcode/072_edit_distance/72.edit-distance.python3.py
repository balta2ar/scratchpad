#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (33.16%)
# Total Accepted:    121.6K
# Total Submissions: 366.6K
# Testcase Example:  '"horse"\n"ros"'
#
# Given two words word1 and word2, find the minimum number of operations
# required to convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
#
#
# Insert a character
# Delete a character
# Replace a character
#
#
# Example 1:
#
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#
#
# Example 2:
#
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
#
#
#


class RecursiveMemoSolution:
    def __init__(self):
        self.memo = {}

    def minDistance(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if (not a) and (not b):  # empty
            return 0
        if a and (not b):  # add to b
            return 1 + self.minDistance(a[1:], b)
        if (not a) and b:  # remove from b
            return 1 + self.minDistance(a, b[1:])
        if a[0] == b[0]:  # 1st char is the same
            return self.minDistance(a[1:], b[1:])
        if (a, b,) in self.memo:
            return self.memo[(a, b)]
        # a has 'x'
        # b has 'y'
        result = 1 + min(
            self.minDistance(a[1:], b[1:]),  # replace 'y' with 'x' in b
            self.minDistance(a, b[1:]),  # remove 'y' from b
            self.minDistance(a[1:], b)  # insert 'x' into b
        )
        self.memo[(a, b)] = result
        return result


class Solution:
    def minDistance(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        m, n = len(a), len(b)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] = 1 + dp[i][j-1]
                elif j == 0:
                    dp[i][j] = 1 + dp[i-1][j]
                elif a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j-1],
                        dp[i][j-1],
                        dp[i-1][j]
                    )

        return dp[m][n]


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().minDistance(*input_), output)


if __name__ == '__main__':
    test(('', 'a'), 1)
    test(('horse', 'ros'), 3)
    test(('intention', 'execution'), 5)
    test(('someverylonganddetailedstring',
          'awesomenotveryablongnedunddailedsting'), 15)
