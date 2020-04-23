from typing import List, Optional


class Solution:
    def bruteForce(self, m, n):
        from functools import reduce
        from operator import __and__
        return reduce(__and__, range(m, n+1))

    def uglyAsFuckingHell(self, m: int, n: int) -> int:
        # return self.bruteForce(m, n)
        from math import log2, pow
        print(m, n, bin(m), bin(n))
        s = int(log2(max(m, n)))
        result = (1 << (s+1)) - 1
        print('s', s)
        while s >= 0:
            sv = 1 << s
            if not (sv & m) or not (sv & n):
                print('remove bit', s)
                result &= ~sv

            if s == 0:
                # special
                print('special')
                if (m & 1 == 0) or (n & 1 == 0):
                    print('remove 1st bin (special)')
                    result &= ~sv
            else:
                lo_mask = ((1 << 32)-1) - ((1 << s)-1)
                hi_mask = (1 << s)-1
                m_lo, m_hi = m & lo_mask, m | hi_mask
                n_lo, n_hi = n & lo_mask, n | hi_mask
                if (not m_lo <= m <= m_hi) or (not n_lo <= n <= n_hi):
                    print('remove bit (second)', s)
                    result &= ~sv

            s -= 1
        print(s)
        print(result, bin(result))
        return result

    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shifts = 0
        while m != n:
            m >>= 1
            n >>= 1
            shifts += 1
        return m << shifts


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    m, n = input_
    result = Solution().rangeBitwiseAnd(m, n)
    assert_eq(result, output)


if __name__ == '__main__':
    test([5, 7], 4)
    test([0, 1], 0)
    test([0, 2147483647], 0)

    from random import choices, seed

    # seed(0); test(choices(range(-50,50), k=100), 10, 11)
    # seed(0); test(choices(range(-50,50), k=1000), 10, 363)
    # seed(0); test(choices(range(-50,50), k=2000), 10, 1437)
    # seed(0); test(choices(range(-50,50), k=3000), 10, 3234)
    # seed(0); test(choices(range(-50,50), k=10000), 10, 23099)
