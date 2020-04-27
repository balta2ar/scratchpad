
# def assert_eq(actual, expected):
#     if actual != expected:
#         raise AssertionError('expected: %s, actual: %s' % (expected, actual))
#
#
# def test(input_, output):
#     assert_eq(Solution().isPalindrome(input_), output)


class SegmentTreeSum:
    def __init__(self, items):
        self.N = len(items)
        self._tree = [0]*2*self.N
        self._items = items
        self.build(0, 0, self.N-1)

    def build(self, node, start, end):
        for i in range(self.N):
            self._tree[self.N+i] = self._items[i]
        for i in range(self.N-1, -1, -1):
            self._tree[i] = self._tree[i << 1] + self._tree[i << 1 | 1]

    def modify(self, p, value):
        p += self.N
        self._tree[p] = value
        while p > 1:
            self._tree[p >> 1] = self._tree[p] + self._tree[p ^ 1]
            p = p >> 1

    def query(self, l, r):
        result = 0

        l, r = l + self.N, r + self.N
        while l < r:
            if l & 1:
                result += self._tree[l]
                l += 1
            if r & 1:
                r -= 1
                result += self._tree[r]
            l, r = l >> 1, r >> 1

        return result

    def __repr__(self):
        return str(self._tree)


def test(tree, start, end, expected_sum):
    # tree = SegmentTreeSum(values)
    result = tree.query(start, end)
    assert result == expected_sum, f'{result} != {expected_sum}'


if __name__ == '__main__':
    a = [1, 1, 1]
    tree = SegmentTreeSum(a)
    test(tree, 0, 1, 1)
    test(tree, 0, 3, 3)
    test(tree, 0, 0, 0)

    a = [1] * 1000
    tree = SegmentTreeSum(a)
    test(tree, 0, 1000, 1000)
    test(tree, 900, 1000, 100)
    test(tree, 0, 100, 100)
    test(tree, 400, 600, 200)

    tree.modify(0, 2)
    test(tree, 0, 1000, 1001)

