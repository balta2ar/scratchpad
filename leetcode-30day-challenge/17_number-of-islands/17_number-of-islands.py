from typing import List, Tuple


class Solution:
    WATER = '0'
    LAND = '1'

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = dict()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                numVisited = self.dfs(grid, visited, row, col, islands)
                if numVisited:
                    islands += 1

        return islands

    def dfs(self, grid, visited, start_row, start_col, mark) -> int:
        front = [(start_row, start_col)]
        numExpanded = 0
        while front:
            row, col = front[0]
            front = front[1:]
            if (row, col) in visited or grid[row][col] == self.WATER:
                continue

            numExpanded += 1
            visited[(row, col)] = mark
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nrow, ncol = row+dy, col+dx
                if 0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]) and grid[nrow][ncol] == self.LAND:
                    front.append((nrow, ncol))

        return numExpanded


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    input_ = list(map(list, input_.split()))
    assert_eq(Solution().numIslands(input_), output)


if __name__ == '__main__':
    test("0", 0)
    test("000", 0)
    test("0\n0\n0", 0)
    test("1\n0\n1", 2)
    test("1", 1)
    test("111", 1)
    test("101", 2)
    test("1\n1\n1", 1)
    test("1\n0\n1", 2)
    test("11110\n11010\n11000\n00000", 1)
    test("11000\n11000\n00100\n00011", 3)
