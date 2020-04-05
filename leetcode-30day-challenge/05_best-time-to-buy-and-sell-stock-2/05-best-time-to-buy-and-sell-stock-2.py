from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        profit = 0
        start = 0
        while start < len(prices):
            current = start + 1
            while current < len(prices) and prices[current] >= prices[current-1]:
                current += 1
            profit += prices[current-1] - prices[start]
            start = current
        return profit


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().maxProfit(input_), output)


if __name__ == '__main__':
    test([7, 1, 5, 3, 6, 4], 7)
    test([1, 2, 3, 4, 5], 4)
    test([7, 6, 4, 3, 1], 0)
