from typing import List


class Solution:
    def fibonacci_loop(self, num):
        if num == 0:
            yield 0
        elif num == 1 or num == 2:
            yield 1
        elif num > 2:
            a = 1 # variable for (n - 1)
            b = 1 # variable for (n - 2)
            yield a
            #yield b
            for _ in range(3, num + 1):
                c = a + b
                a, b = b, c
                yield c

    def minStartValue(self, nums: List[int]) -> int:
        minPos = nums[0]
        rollSum = nums[0]
        for x in nums[1:]:
            rollSum += x
            minPos = min(minPos, rollSum)
        if minPos >= 1:
            return 1
        return -minPos + 1


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().minStartValue(input_), output)


if __name__ == '__main__':
    test([-3, 2, -3, 4, 2], 5)
    test([0], 1)
    test([-5], 6)
    test([1, 2], 1)
    test([1, -2, -3], 5)
