from typing import List, Optional


class Solution:
    def bruteForce(self, nums, k):
        count = 0
        for i in range(len(nums)+1):
            for j in range(i):
                sum_ = sum(nums[j:i])
                if sum_ == k:
                    count += 1
        return count

    def withPrefixSum(self, nums, k):
        from itertools import accumulate
        prefixSum = [0] + list(accumulate(nums))
        count = 0
        for i in range(len(prefixSum)):
            for j in range(i):
                sum_ = prefixSum[i] - prefixSum[j]
                if sum_ == k:
                    count += 1
        return count

    def withPrefixSumAndHashTable(self, nums, k):
        from itertools import accumulate
        from collections import defaultdict
        prefixSum = list(accumulate(nums))
        seenSum = defaultdict(int)
        count = 0
        for i in range(len(prefixSum)):
            val = prefixSum[i]
            if val == k:
                count += 1

            # at this point we are at position i (0 < j < i < N)
            # the current prefix sum is val. it may very well be that
            # val > k, in which case we need the missing part (val - k)
            # to complete the current prefix sum with a previous prefix sum.
            toK = val - k
            if toK in seenSum:
                count += seenSum[toK]
            seenSum[val] += 1
        return count

    def subarraySum(self, nums: List[int], k: int) -> int:
        # return self.bruteForce(nums, k)
        # return self.withPrefixSum(nums, k)
        return self.withPrefixSumAndHashTable(nums, k)


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, k, output):
    result = Solution().subarraySum(input_, k)
    assert_eq(result, output)


if __name__ == '__main__':
    test([0, 0], 0, 3)
    test([1, 1, 1], 1, 3)
    test([1, 1, 1], 2, 2)
    test([0, 0, 0], 0, 6)
    test([0, 0, 0, 0], 0, 10)
    test([0, 0, 0, 0, 0], 0, 15)
    test([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0, 55)
    from random import seed, choices
    # seed(0); test(choices(range(-50,50), k=100), 10, 11)
    # seed(0); test(choices(range(-50,50), k=1000), 10, 363)
    # seed(0); test(choices(range(-50,50), k=2000), 10, 1437)
    # seed(0); test(choices(range(-50,50), k=3000), 10, 3234)
    # seed(0); test(choices(range(-50,50), k=10000), 10, 23099)
