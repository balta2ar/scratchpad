from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # print(nums, target)
        lo, hi = 0, len(nums)-1

        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        while lo < hi:
            mid = int((lo + hi) / 2)
            # print(lo, mid, hi)
            if nums[mid] == target:
                return mid
            if nums[lo] == target:
                return lo
            if nums[hi] == target:
                return hi

            left = nums[lo] <= nums[mid]
            right = nums[mid] <= nums[hi]
            if left:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid-1
                else:
                    lo = mid+1
            if right:
                if nums[mid] <= target <= nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1


        return -1


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, target, output):
    assert_eq(Solution().search(input_, target), output)


if __name__ == '__main__':
    test([4], 4, 0)

    test([4, 5, 6, 7, 0, 1, 2], 0, 4)
    test([4, 5, 6, 7, 0, 1, 2], 1, 5)
    test([4, 5, 6, 7, 0, 1, 2], 2, 6)
    test([4, 5, 6, 7, 0, 1, 2], 4, 0)
    test([4, 5, 6, 7, 0, 1, 2], 5, 1)
    test([4, 5, 6, 7, 0, 1, 2], 6, 2)
    test([4, 5, 6, 7, 0, 1, 2], 7, 3)
    test([4, 5, 6, 7, 0, 1, 2], 3, -1)
    test([4, 5, 6, 7, 0, 1, 2], 13, -1)
    test([4, 5, 6, 7, 0, 1, 2], -1, -1)
