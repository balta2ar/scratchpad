from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        from heapq import heapify, heappop, heappush
        h = [-x for x in stones]
        heapify(h)

        while len(h) > 1:
            x = -heappop(h)
            y = -heappop(h)
            if x != y:
                heappush(h, -abs(x-y))

        return -h[0] if h else 0


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().lastStoneWeight(input_), output)


if __name__ == '__main__':
    test([2, 7, 4, 1, 8, 1], 1)
