from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonzeros = 0
        for i, value in enumerate(nums):
            if value != 0:
                nums[nonzeros], nums[i] = nums[i], nums[nonzeros]
                nonzeros += 1


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    Solution().moveZeroes(input_)
    assert_eq(input_, output)


if __name__ == '__main__':
    test([0, 1, 0, 3, 12], [1, 3, 12, 0, 0])
    test([0, 0, 12], [12, 0, 0])
    test([0, 0], [0, 0])
    test([0], [0])
    test([1], [1])
    test([0, 1, 0, 3, 0], [1, 3, 0, 0, 0])
    test([1, 0, 0, 0], [1, 0, 0, 0])
    test([0, 0, 0, 1], [1, 0, 0, 0])
