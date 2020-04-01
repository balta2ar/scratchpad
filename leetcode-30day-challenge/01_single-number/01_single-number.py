from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from functools import reduce
        return reduce(lambda a, b: a ^ b, nums)


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().singleNumber(input_), output)


if __name__ == '__main__':
    test([2, 2, 1], 1)
    test([4, 1, 2, 1, 2], 4)
