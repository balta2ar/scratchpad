from typing import List


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        si, ti = len(S)-1, len(T)-1
        skips, skipt = 0, 0

        def roll(X, idx):
            skip = 0
            while idx >= 0:
                if X[idx] == '#':
                    print('idx BS %s %s' % (X[idx], skip,))
                    idx -= 1
                    skip += 1
                elif skip > 0:
                    print('idx skip %s' % (X[idx],))
                    idx -= 1
                    skip -= 1
                else:
                    break
            return idx

        while si >= 0 and ti >= 0:
            si = roll(S, si)
            ti = roll(T, ti)
            if (si >= 0) ^ (ti >= 0) == 1:
                print('INCONSIST %s %s' % (si, ti))
                return False
            if si >= 0 and ti >= 0 and S[si] != T[ti]:
                print('NOT MATCH %s %s' % (S[si], T[ti]))
                return False
            print('round %s %s' % (S[si], T[ti]))
            si -= 1
            ti -= 1

        si = roll(S, si)
        ti = roll(T, ti)
        print(si, ti)
        return si < 0 and ti < 0 and (si == ti)


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(inputS, inputT, output):
    assert_eq(Solution().backspaceCompare(inputS, inputT), output)


if __name__ == '__main__':
    test("bbbextm", "bbb#extm", False)
    test("nzp#o#g", "b#nzp#o#g", True)
    test("bxj##tw", "bxj###tw", False)
    test("bxj##tw", "bxo#j##tw", True)
    test("xywrrmp", "xywrrmu#p", True)
    test("ab#c", "ad#c", True)
    test("ab##", "c#d#", True)
    test("a##c", "#a#c", True)
    test("a#c", "b", False)
