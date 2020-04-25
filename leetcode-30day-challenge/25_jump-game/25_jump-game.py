from typing import List, Optional


class Solution:
    def canJumpBruteForce(self, nums: List[int]) -> bool:
        reachable = [False] * len(nums)
        reachable[0] = True

        for i, v in enumerate(nums):
            if not reachable[i]:
                continue
            remains = len(nums) - i
            limit = min(i+remains, i+1+v)
            for j in range(i+1, limit):
                reachable[j] = True

        return reachable[-1]

    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        hi = 0

        for i, v in enumerate(nums):
            if i > hi: break
            hi = max(hi, i+v)

        return hi >= len(nums)-1


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    result = Solution().canJump(input_)
    assert_eq(result, output)


if __name__ == '__main__':
    test([2, 0, 0], True)
    test([0, 2, 3], False)
    test([0], True)
    test([2, 3, 1, 1, 4], True)
    test([3, 2, 1, 0, 4], False)
