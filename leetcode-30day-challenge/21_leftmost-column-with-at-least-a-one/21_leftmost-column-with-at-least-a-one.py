from typing import List, Optional


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
    def __init__(self, matrix):
        self._matrix = matrix
        self._num_calls = 0

    def get(self, x: int, y: int) -> int:
        self._num_calls += 1
        if self._num_calls > 1000:
            raise RuntimeError('Num calls too large')
        return self._matrix[x][y]

    def dimensions(self) -> List[int]:
        return [len(self._matrix), len(self._matrix[0])]


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        x, y = 0, m-1
        last_col = -1
        # print(n, m, binaryMatrix._matrix)
        while x < n and y >= 0:
            val = binaryMatrix.get(x, y)
            if val == 1:
                last_col = y
                y -= 1
                # print('move col left', x, y)
            elif val == 0:
                x += 1
                # print('move row down', x, y)
            else:
                raise RuntimeError('Unexpected value %s' % (val,))
        return last_col


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    result = Solution().leftMostColumnWithOne(BinaryMatrix(input_))
    assert_eq(result, output)


if __name__ == '__main__':
    test([[0, 0], [1, 1]], 0)
    test([[0, 0], [0, 1]], 1)
    test([[0, 0], [0, 0]], -1)
    test([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]], 1)
