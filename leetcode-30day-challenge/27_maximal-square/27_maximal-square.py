from typing import List, Optional


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # print(matrix)
        n = len(matrix)
        if not n: return 0
        m = len(matrix[0])
        if not m: return 0
        d = [[0] * m for _ in range(n)]
        best = 0
        for i in range(n):
            d[i][0] = 1 if int(matrix[i][0]) == 1 else 0
            best = max(best, d[i][0])
        for i in range(m):
            d[0][i] = 1 if int(matrix[0][i]) == 1 else 0
            best = max(best, d[0][i])
        # print(d)
        # print(best)

        for i in range(1, n):
            for j in range(1, m):
                # c b
                # a x
                x = int(matrix[i][j])
                if x == 0:
                    d[i][j] = 0
                    continue

                # print('>>', i, j, x)
                a, b, c = d[i][j-1], d[i-1][j], d[i-1][j-1]
                if 0 in (a, b, c):
                    d[i][j] = 1
                else:
                    # print('no zero')
                    if a == b == c:
                        # print('a+1', a+1)
                        d[i][j] = a+1
                    else:
                        # print('min+1', min(a,b,c)+1)
                        d[i][j] = min(a, b, c)+1
                x = d[i][j]-1
                # print(x, best)
                if best == 0: best = x+1
                elif a == b == c == x and x > 0: best = max(best, x+1)
        # print(d)
        # print(best)

        return best*best


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input1, output):
    result = Solution().maximalSquare(input1)
    assert_eq(result, output)


if __name__ == '__main__':

    test([["0","0","0","0","0"],
          ["0","0","0","0","0"],
          ["0","0","0","0","1"],
          ["0","0","0","0","0"]], 1)

    test([["1", "1"], ["1", "1"]], 4)
    test([[1]], 1)
    test([["1"]], 1)
    m = [[1, 0, 1, 0, 0],
         [1, 0, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 0, 0, 1, 0], ]
    test(m, 4)
    m = [["1", "0", "1", "0", "0"],
         ["1", "0", "1", "1", "1"],
         ["1", "1", "1", "1", "1"],
         ["1", "0", "0", "1", "0"], ]
    test(m, 4)
    test([], 0)
    test([[]], 0)
    test([[0]], 0)
    test([["0"]], 0)
    #[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
