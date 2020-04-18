from typing import List


class SolutionDP:
    def fibonacci_loop(self, num):
        if num == 0:
            yield 0
        elif num == 1 or num == 2:
            yield 1
        elif num > 2:
            a = 1 # variable for (n - 1)
            b = 1 # variable for (n - 2)
            yield a
            for _ in range(3, num + 1):
                c = a + b
                a, b = b, c
                yield c

    def findMinFibonacciNumbers(self, k: int) -> int:
        from itertools import takewhile
        fibs = list(takewhile(lambda x: x <= k, self.fibonacci_loop(999999)))
        # print(k, fibs)
        m = [[0.0] * (k+1) for _ in range(len(fibs)+1)]
        for i in range(1, k+1):
            m[0][i] = float('inf')

        for c in range(1, len(fibs)+1):
            for r in range(1, k+1):
                if fibs[c-1] == r: # coin is exactly the value r
                    m[c][r] = 1
                elif fibs[c-1] > r: # coin is too large, can't be used
                    m[c][r] = m[c-1][r]
                else:
                    # coin is smaller than r, it can be used, let's consider
                    # what's best:
                    m[c][r] = min(
                        m[c-1][r], # skip the coin
                        1+m[c][r-fibs[c-1]] # same coin with smaller value of r
                    )
        # for l in m:
        #     print(l)

        return int(m[-1][-1])

class Solution:
    def fibonacci_loop(self, num):
        if num == 0:
            yield 0
        elif num == 1 or num == 2:
            yield 1
        elif num > 2:
            a = 1 # variable for (n - 1)
            b = 1 # variable for (n - 2)
            yield a
            for _ in range(3, num + 1):
                c = a + b
                a, b = b, c
                yield c

    def findMinFibonacciNumbers(self, k: int) -> int:
        from itertools import takewhile
        fibs = list(takewhile(lambda x: x <= k, self.fibonacci_loop(999999)))
        sumK = 0
        index = len(fibs)-1
        while k > 0:
            f = fibs[index]
            if f <= k:
                k -= f
                sumK += 1
            index -= 1
        return sumK


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().findMinFibonacciNumbers(input_), output)


if __name__ == '__main__':
    # 1 2 3 5 8 13 21 34
    test(5, 1)
    test(7, 2)
    test(10, 2)
    test(11, 2)
    test(15, 2)
    test(19, 3)
    test(374602, 9)

