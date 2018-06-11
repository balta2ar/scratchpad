#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (27.63%)
# Total Accepted:    214K
# Total Submissions: 773.9K
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
#
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a
# number of rows:
#
#
# string convert(string s, int numRows);
#
# Example 1:
#
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#
#
# Example 2:
#
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#
#


class Solution:
    def convert(self, s, num_rows):
        """
        :type s: str
        :type num_rows: int
        :rtype: str
        """
        n = num_rows
        c = len(s)
        step = 2 * n - 2
        output = []

        if n == 1:
            return s

        def put(index):
            if index < c:
                output.append(s[index])

        # The idea of this method is to calculate desination indices for each
        # source character. First and last row indices are easy as they contain
        # only one character per loop. Indices in the middle are a little
        # trickier as there are two indicies per loop.

        for offset in range(0, c, step):
            put(offset)

        for i in range(1, n-1):
            for offset in range(0, c, step):
                first = offset + i
                second = offset + 2*n - 2 - i
                put(first)
                if first != second:
                    put(second)

        for offset in range(n-1, c, step):
            put(offset)

        # There is another, simpler approach.
        # 1. Allocate n buffers, one per each row
        # 2. Iterate over all characters of s
        # 3. Keep an index of the current buffer and a step (direction).
        #    You start with the buffer 0, and step 1. When you reach
        #    buffer n-1, set step to -1.
        # This way you will be oscillating between buffers and putting
        # chracters into corresponding ones.

        return ''.join(output)


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, num_rows, output):
    assert_eq(Solution().convert(input_, num_rows), output)


if __name__ == '__main__':
    test('123', 1, '123')
    test('1234', 2, '1324')
    test('12345678', 3, '15246837')
    test('123456789abcde', 4, '17d268ce359b4a')
    test('123456789abcdef', 4, '17d268ce359bf4a')
    test('123456789abcdefg', 4, '17d268ce359bf4ag')
