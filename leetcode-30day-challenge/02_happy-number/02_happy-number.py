from typing import List


def sum_squares(x: int) -> int:
    result = 0
    while x > 0:
        rem = x % 10
        result += rem * rem
        x = int(x / 10)
    return result

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum_squares(n)
            if n == 1:
                return True

        return False


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().isHappy(input_), output)


if __name__ == '__main__':
    test(19, True)
    test(2, False)
    test(1, True)
