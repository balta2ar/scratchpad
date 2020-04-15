from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums

        result = nums[:]
        for i in range(len(nums) - 2, -1, -1):
            result[i] = result[i] * result[i+1]
        for i in range(1, len(nums)):
            nums[i] = nums[i] * nums[i-1]
        for i in range(0, len(nums)):
            left = nums[i-1] if i > 0 else 1
            right = result[i+1] if i < len(result)-1 else 1
            result[i] = left * right

        return result


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().productExceptSelf(input_), output)


if __name__ == '__main__':
    test([1, 2, 3, 4], [24, 12, 8, 6])
    test([4], [4])
    test([3, 4], [4, 3])
