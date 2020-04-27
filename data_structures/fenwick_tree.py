class FenwickTree:
    def __init__(self, n):
        self._n = n
        self._xs = [0] * (n+1)

    def add(self, at, value):
        # at is zero-based. we convert it to our 1-based
        at = at+1
        while at <= self._n:
            self._xs[at] += value
            at += at & -at
        print(self._xs)

    def sum(self, upto):
        # upto is zero-based. we convert it to our 1-based
        result = 0
        upto = upto+1
        while upto > 0:
            result += self._xs[upto]
            upto -= upto & -upto
        return result


def assert_eq(expected, actual):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


# def test(input_, output):
#     assert_eq(Solution().isPalindrome(input_), output)


if __name__ == '__main__':
    xs = [1, 2, 3, 4, 5]
    tree = FenwickTree(len(xs))
    for i, x in enumerate(xs):
        tree.add(i, x)
    assert_eq(1, tree.sum(0))
    assert_eq(3, tree.sum(1))
    assert_eq(6, tree.sum(2))
    assert_eq(10, tree.sum(3))
    assert_eq(15, tree.sum(4))
    tree.add(0, 9)
    assert_eq(10, tree.sum(0))
    tree.add(1, 1)
    assert_eq(25, tree.sum(4))
