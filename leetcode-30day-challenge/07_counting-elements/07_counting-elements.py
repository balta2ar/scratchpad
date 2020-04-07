from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        from collections import defaultdict

        seen = defaultdict(int)
        for x in arr:
            seen[x] = 0
        for x in arr:
            if x+1 in seen:
                seen[x+1] += 1
        return sum(seen.values())


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().countElements(input_), output)


if __name__ == '__main__':
    test([1, 3, 2, 3, 5, 0], 3)
    test([1, 2, 3], 2)
    test([1, 1, 3, 3, 5, 5, 7, 7], 0)
    test([1, 1, 2, 2], 2)
