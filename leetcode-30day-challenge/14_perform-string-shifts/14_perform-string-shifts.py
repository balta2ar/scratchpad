from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        index = 0
        for sh in shift:
            direction, amount = sh
            amount = amount % len(s)
            if direction == 0: # left
                index += amount
            elif direction == 1: # right
                index -= amount
            index = index % len(s)
        return s[index:] + s[:index]


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, shift, output):
    assert_eq(Solution().stringShift(input_, shift), output)


if __name__ == '__main__':
    test("abc", [[0, 1], [1, 2]], "cab")
    test("abcdefg", [[1, 1], [1, 1], [0, 2], [1, 3]], "efgabcd")
