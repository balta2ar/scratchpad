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


class SolutionDivideAndConquer:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        base = 0
        def helper(left, right):
            if right - left <= 2:
                m = max(nums[left:right])
                l = max(base, nums[left])
                f = sum(nums[left:right])
                c = max(nums[left:right])
                r = max(base, nums[right-1])
                return m, l, f, c, r

            mid = left + int((right - left) / 2)
            amax, al, af, ac, ar = helper(left, mid)
            bmax, bl, bf, bc, br = helper(mid, right)
            m, l, f, c, r = (
                max(amax, bmax),               # max
                max(al, af, af + bl, af + bf), # left
                af + bf,                       # full
                max(ac, ar + bl, bc),          # center
                max(br, bf, ar + bf, af + bf), # right
            )
            return m, l, f, c, r

        m, l, f, c, r = helper(0, len(nums))
        result = max(l, f, c, r)
        # if all numbers were negative, set result to the max negative number
        if m < 0 and m < result:
            result = m
        return result


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    #assert_eq(Solution().maxSubArray(input_), output)
    assert_eq(SolutionDivideAndConquer().maxSubArray(input_), output)


if __name__ == '__main__':
    test([-2, -2, -3, 0, -3, 1, -3], 1)
    test([1, 2, 3, -10, 1, 2, 4], 7)

    test([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
    test([1, 2, 3], 6)
    test([1], 1)
    test([-3], -3)
    test([-1, 0, -3], 0)
    test([-1, 1, -3], 1)
    test([-1, -3], -1)
    test([1, 2, 3, -10, 1, 2, 4], 7)
    test([1, 2, 4, -10, 1, 2, 3], 7)
    test([2, -1, -3], 2)
    test([-1, -3, 2], 2)
