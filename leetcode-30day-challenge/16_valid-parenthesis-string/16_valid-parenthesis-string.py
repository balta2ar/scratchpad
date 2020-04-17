from typing import List, Tuple


class FailedSolution1:
    def checkValidString(self, s: str) -> bool:
        valid, more = self.validate(s)
        if not more:
            return valid

        print('second run with more', more)
        valid, more = self.validate(self.reverse(more))
        if not more:
            return valid

        raise RuntimeError('not more 2nd time')

    def validate(self, s: str) -> Tuple[bool, str]:
        if not s:
            return True, ''

        print('validating', s)
        stack = []
        self.stars = 0
        right = []
        for c in s:
            if c == '(':
                stack.append('(')
            elif c == '*':
                self.stars += 1
                stack.append('*')
            elif c == ')':
                if stack:
                    if stack[-1] == '*':
                        right.append(stack[-1])
                    else:
                        stack.pop()
                else:
                    if self.recover():
                        continue
                    else:
                        return False, ''
            else:
                raise RuntimeError('Unexpected symbol: %s' % (c,))
        print('at the end stack', stack, 'right', right)
        return stack == 0, ''.join(stack) + ''.join(right)

    def recover(self):
        if self.stars > 0:
            self.stars -= 1
            return True
        return False

    def reverse(self, s):
        result = []
        for c in reversed(s):
            if c == '(':
                result.append(')')
            elif c == ')':
                result.append('(')
            else:
                result.append(c)
        return ''.join(result)


class Solution:
    def checkValidString(self, s: str) -> bool:
        # left brackets margin: low & high
        # low means the number of actual open left brackes
        # high means the number of potential open left branches (due to *)
        low, high = 0, 0
        for c in s:
            if c in '(':
                low += 1
                high += 1
            elif c in '*':
                # low may go below 0 here, but we limit it to be at least zero
                # later in the loop
                low -= 1 # could be )
                high += 1 # could be (
            elif c in ')':
                low -= 1
                high -= 1
            if high < 0:
                # case: too many closing parenthesis
                break
            low = max(0, low)
        # case: if low > 0, it means there are opening parenthesis
        return low == 0


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().checkValidString(input_), output)


if __name__ == '__main__':
    test(")))", False)
    test("(*)))", False)
    test("(*()", True)
    test("((*)", True)
    test("", True)
    test("*", True)
    test("***", True)
    test("()", True)
    test("(*)", True)
    test("(*))", True)
    test("()*)", True)
