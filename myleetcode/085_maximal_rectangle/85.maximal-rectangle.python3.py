#
# [85] Maximal Rectangle
#
# https://leetcode.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (30.10%)
# Total Accepted:    89.9K
# Total Submissions: 298.5K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],
#                      ["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
# containing only 1's and return its area.
#
# Example:
#
#
# Input:
# [
# ⁠ ["1","0","1","0","0"],
# ⁠ ["1","0","1","1","1"],
# ⁠ ["1","1","1","1","1"],
# ⁠ ["1","0","0","1","0"]
# ]
# Output: 6
#
#
#


class SolutionSlow:
    def addp(self, a, b):
        return list(map(lambda x: x[0]+x[1], zip(a, b)))

    def get_area(self, rect):
        lrow, lcol, rrow, rcol = rect
        return (rrow - lrow + 1) * (rcol - lcol + 1)

    def is_valid(self, rect: list, grid):
        lrow, lcol, rrow, rcol = rect
        n, m = len(grid), len(grid[0])
        # print('is_valid', rect)
        if not 0 <= lrow <= rrow < n:
            return False
        if not 0 <= lcol <= rcol < m:
            return False
        invalid = "0"
        for i in range(lrow, rrow+1):
            if grid[i][lcol] == invalid:
                return False
            if grid[i][rcol] == invalid:
                return False
        for i in range(lcol+1, rcol):
            if grid[lrow][i] == invalid:
                return False
            if grid[rrow][i] == invalid:
                return False
        return True

    def expand(self, i, j, grid, mxs):
        rect = [i, j, i, j]
        # print('expand', rect)
        if not self.is_valid(rect, grid):
            return 0
        for m in mxs:
            new_rect = self.addp(rect, m)
            while self.is_valid(new_rect, grid):
                # print('new_rect', new_rect)
                rect = new_rect
                new_rect = self.addp(rect, m)
        return self.get_area(rect)

    def maximalRectangle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        exph = [[-1, 0, 0, 0], [0, 0, 1, 0], [0, -1, 0, 0], [0, 0, 0, 1]]
        expv = [[0, -1, 0, 0], [0, 0, 0, 1], [-1, 0, 0, 0], [0, 0, 1, 0]]
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        area = 0
        for i in range(n):
            for j in range(m):
                area = max(area, self.expand(i, j, grid, exph))
                area = max(area, self.expand(i, j, grid, expv))
        return area


class Solution:
    def maximalRectangle(self, grid):
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        left = [[0]*m for _ in range(n)]
        up = [[0]*m for _ in range(n)]
        max_area = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0':
                    # reset the sequence
                    left[i][j] = up[i][j] = 0
                else:
                    # count the len of the sequence of 1s to the left and up
                    left[i][j] = 1 + (left[i][j-1] if j > 0 else 0)
                    up[i][j] = 1 + (up[i-1][j] if i > 0 else 0)

                    # we can't simply multiply left by up in this cell because
                    # the width given in "left" may not span on the lines
                    # given in "up". this we iterate over the cells upwards,
                    # keep the min width and calculate the area.
                    min_width = left[i][j]
                    for k in range(up[i][j]):
                        min_width = min(min_width, left[i-k][j])
                        area = min_width * (k+1)
                        max_area = max(max_area, area)

        return max_area


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().maximalRectangle(input_), output)


if __name__ == '__main__':
    test([["0", "1"]], 1)
    test([["0"]], 0)
    test([["0", "0", "1", "0"],
          ["1", "1", "1", "1"],
          ["1", "1", "1", "1"],
          ["1", "1", "1", "0"],
          ["1", "1", "0", "0"],
          ["1", "1", "1", "1"],
          ["1", "1", "1", "0"]], 12)
    test([], 0)
    test([["1", "0", "1", "0", "0"],
          ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["1", "0", "0", "1", "0"]], 6)
