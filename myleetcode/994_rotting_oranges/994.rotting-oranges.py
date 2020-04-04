#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Easy (46.98%)
# Total Accepted:    66.1K
# Total Submissions: 140.7K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# In a given grid, each cell can have one of three values:
#
#
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
#
#
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
# orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange.  If this is impossible, return -1 instead.
#
#
#
#
# Example 1:
#
#
#
#
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
#
#
#
# Example 2:
#
#
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
#
#
#
# Example 3:
#
#
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the
# answer is just 0.
#
#
#
#
# Note:
#
#
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.
#
#
#
#
#
from typing import List


class Solution:
    EMPTY = 0
    FRESH = 1
    ROTTEN = 2

    def orangesRotting(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])

        def neighbors(x, y):
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < width) and (0 <= ny < height):
                    yield nx, ny

        def state_to_string():
            s = ''
            for y, row in enumerate(grid):
                for x, state in enumerate(row):
                    s += ' %d ' % state
                s += '\n'
            return s

        round_number = 0
        # print(state_to_string())
        while True:
            got_rotten = set()
            fresh_remains = set()
            # print('starting round %s' % round_number)

            for y, row in enumerate(grid):
                for x, state in enumerate(row):
                    if state == self.ROTTEN:
                        for nx, ny in neighbors(x, y):
                            n_value = grid[ny][nx]
                            if n_value == self.FRESH:
                                got_rotten.add((nx, ny))
                    elif state == self.FRESH:
                        fresh_remains.add((x, y))

            # print('got rotten %s' % got_rotten)
            # print('fresh_remains %s' % fresh_remains)
            if len(got_rotten) == 0:
                if fresh_remains:
                    # unreachable fresh fruits
                    return -1
                # all fresh are rotten, all are reachable
                return round_number

            for x, y in got_rotten:
                value = grid[y][x]
                if value == self.FRESH:
                    grid[y][x] = self.ROTTEN
                    if (x, y) in fresh_remains:
                        fresh_remains.remove((x, y))
                else:
                    raise RuntimeError('Unexpected state %s at %s' % (value, (x, y)))

            # print(state_to_string())
            round_number += 1
            # if round_number > 50:
            #     raise RuntimeError('Too many rounds %s' % round_number)


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().orangesRotting(input_), output)


if __name__ == '__main__':
    test([[1, 2]], 1)
    test([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4)
    test([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1)
    test([[0, 2]], 0)
