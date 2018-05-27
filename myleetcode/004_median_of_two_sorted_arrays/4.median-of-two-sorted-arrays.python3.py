#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (23.24%)
# Total Accepted:    262.1K
# Total Submissions: 1.1M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
#
#
#
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
#
#
#


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # The way it's explained on leetcode discussion is a bit difficult to
        # grasp at first. But the idea is simple: because median is the middle
        # value in a sorted array, and because we have two sorted arrays,
        # we need to find a split of these two arrays, such that:
        # 1. the length of left two parts == the lenght of right two parts.
        #    This condition is to make sure that we select an item in the
        #    middle.
        # 2. all items in the left two parts are smaller than all items in the
        #    right two parts.
        #    This condition is to make sure that parts do not overlap.
        # Edgecases when one array is empty are handled by using
        # -infinity/+infinity when searching an item.
        # Finally, we can do the binary search over the smaller array (swap
        # arguments if necessary) to find such split point i.
        #
        # A very good explanation: https://www.youtube.com/watch?v=LPFhl65R7ww
        M, N = len(nums1), len(nums2)

        if M + N == 1:
            both = nums1 + nums2
            return float(both[0])

        if M > N:
            return self.findMedianSortedArrays(nums2, nums1)
        odd = bool((M + N) % 2)
        start, end = 0, M

        while start <= end:
            i = (start + end) // 2
            j = (M + N + 1) // 2 - i
            max_left_a = float('-inf') if i == 0 else nums1[i-1]
            min_right_a = float('+inf') if i == M else nums1[i]
            max_left_b = float('-inf') if j == 0 else nums2[j-1]
            min_right_b = float('+inf') if j == N else nums2[j]

            if max_left_a <= min_right_b and max_left_b <= min_right_a:
                if odd:
                    return float(max(max_left_a, max_left_b))

                return (max(max_left_a, max_left_b) +
                        min(min_right_a, min_right_b)) / 2.0
            elif max_left_a > min_right_b:
                # move to the left
                end = i - 1
            else:
                start = i + 1


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(a, b):
    from statistics import median
    assert_eq(Solution().findMedianSortedArrays(a, b), median(sorted((a + b))))


if __name__ == '__main__':
    test([1, 3], [2])
    test([1, 2], [3, 4])
    test([], [1])
    test([1], [])
    test([], [1, 2, 3, 4, 5])
    test([1, 2, 3, 4, 5], [])
