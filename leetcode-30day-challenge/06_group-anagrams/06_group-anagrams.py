from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        groups = defaultdict(list)

        for item in strs:
            sitem = ''.join(sorted(item))
            groups[sitem].append(item)

        return list(map(list, list(groups.values())))


def assert_eq(actual, expected):
    actual = sorted([sorted(x) for x in actual])
    expected = sorted([sorted(x) for x in expected])

    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().groupAnagrams(input_), output)


if __name__ == '__main__':
    test(["", ""], [["", ""]])
    test(["eat", "tea", "tan", "ate", "nat", "bat"], [
        ["ate", "eat", "tea"],
        ["tan", "nat"],
        ["bat"]
    ])
