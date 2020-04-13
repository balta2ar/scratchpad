from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = dict()
        count = 0
        best = 0
        for i, v in enumerate(nums):
            count += 1 if v == 1 else -1
            if count == 0:
                best = max(best, i+1)
            elif count in seen:
                best = max(best, i-seen[count])
            else:
                seen[count] = i
        return best

def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().findMaxLength(input_), output)


if __name__ == '__main__':
    test([0, 1, 0, 1], 4)
    test([0, 1, 1], 2)
    test([0, 0, 0, 1, 1, 1, 0], 6)
    test([1, 1, 0, 0, 0, 0, 1, 1, 1, 0], 10)
    test([1, 1, 0, 0, 0, 0, 1, 1, 1], 8)
    test([0, 1], 2)
    test([0, 1, 0], 2)
    test([0, 1, 0, 1, 1, 0, 1, 0, 1, 0], 10)
    test([0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0], 12)
