from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left, right = 0, 1
        current_sum, best_sum = nums[0], nums[0]
        while left < len(nums):
            while right < len(nums) and current_sum >= 0:
                current_sum += nums[right]
                best_sum = max(best_sum, current_sum)
                right += 1
            while (left < right) and (current_sum < 0 or right == len(nums)):
                current_sum -= nums[left]
                left += 1
                if left < right:
                    best_sum = max(best_sum, current_sum)
        return best_sum


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().maxSubArray(input_), output)


if __name__ == '__main__':
    test([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
    test([1, 2, 3], 6)
    test([1], 1)
    test([-3], -3)
    test([-1, -3], -1)
    test([1, 2, 3, -10, 1, 2, 4], 7)
    test([1, 2, 4, -10, 1, 2, 3], 7)
    test([2, -1, -3], 2)
    test([-1, -3, 2], 2)
