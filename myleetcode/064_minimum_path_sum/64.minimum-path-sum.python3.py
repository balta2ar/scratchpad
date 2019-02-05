#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (41.63%)
# Total Accepted:    157.2K
# Total Submissions: 377.7K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example:
#
#
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
#
#
#


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        from copy import deepcopy
        dp = deepcopy(grid)

        for i in range(1, m):
            dp[0][i] += dp[0][i-1]
        for i in range(1, n):
            dp[i][0] += dp[i-1][0]

        for ni in range(1, n):
            for mi in range(1, m):
                dp[ni][mi] = min(
                    dp[ni][mi-1] + dp[ni][mi],
                    dp[ni-1][mi] + dp[ni][mi])

        return dp[n-1][m-1]


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().minPathSum(input_), output)


if __name__ == '__main__':
    test([[1, 3, 1],
          [1, 5, 1],
          [4, 2, 1]], 7)
