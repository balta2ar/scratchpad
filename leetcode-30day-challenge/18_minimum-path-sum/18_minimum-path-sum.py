from typing import List, Tuple


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0 and col == 0:
                    continue
                options = []
                if row > 0: options.append(grid[row][col] + grid[row-1][col])
                if col > 0: options.append(grid[row][col] + grid[row][col-1])
                grid[row][col] = min(options)
        return grid[-1][-1]


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().minPathSum(input_), output)


if __name__ == '__main__':
    test([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ], 7)
    test([
        [1, 3, 9],
        [1, 5, 1],
        [4, 2, 1]
    ], 9)
    test([
        [1, 3, 9],
        [1, 6, 1],
        [4, 9, 1]
    ], 10)
