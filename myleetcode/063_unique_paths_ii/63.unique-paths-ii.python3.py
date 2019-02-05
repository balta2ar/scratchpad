#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (32.34%)
# Total Accepted:    141.6K
# Total Submissions: 438K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
#
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
#
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
#
#
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# Note: m and n will be at most 100.
#
# Example 1:
#
#
# Input:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#
#
#


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[1]*m for _ in range(n)]
        if obstacleGrid[0][0] == 1:
            dp[0][0] = 0

        for i in range(1, m):
            if obstacleGrid[0][i] == 1:
                dp[0][i] = 0
            else:
                dp[0][i] = dp[0][i-1]
        for i in range(1, n):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0]

        for ni in range(1, n):
            for mi in range(1, m):
                if obstacleGrid[ni][mi] == 1:
                    dp[ni][mi] = 0
                else:
                    dp[ni][mi] = dp[ni][mi-1] + dp[ni-1][mi]

        return dp[n-1][m-1]


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().uniquePathsWithObstacles(input_), output)


if __name__ == '__main__':
    test([[1]], 0)
    test([[0, 0, 0],
          [0, 1, 0],
          [0, 0, 0]], 2)
    test([[0, 1, 0],
          [0, 1, 0],
          [0, 0, 0]], 1)
    test([[0, 0, 0],
          [0, 1, 0],
          [1, 0, 0]], 1)
