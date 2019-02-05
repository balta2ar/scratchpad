#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (37.24%)
# Total Accepted:    206.7K
# Total Submissions: 554.9K
# Testcase Example:  '[1,1]'
#
# Given n non-negative integers a1, a2, ..., an, where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#
#


class Solution:
    def maxArea(self, h):
        """
        :type h: List[int]
        :rtype: int
        """
        left, right = 0, len(h) - 1
        maxarea = 0

        # Use left and right pointer to calculate maximum area. Then
        # move pointer that points to the smaller wall closer to another
        # pointer.

        while left < right:
            area = (right - left) * min(h[left], h[right])
            maxarea = max(area, maxarea)
            if h[left] < h[right]:
                left += 1
            else:
                right -= 1

        return maxarea


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().maxArea(input_), output)


# if __name__ == '__main__':
#     test([1, 1], 1)
#     test([1, 2, 3, 4], 6-1)
