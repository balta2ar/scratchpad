from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        left = str(self.left)
        right = str(self.right)
        left = '\n'.join('    L %s' % (line,) for line in left.splitlines())
        right = '\n'.join('    R %s' % (line,) for line in right.splitlines())
        return '%s\n%s\n%s\n' % (str(self.val), left, right)


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.index = 0
        return self.helper(preorder, float('-inf'), float('+inf'))

    def helper(self, preorder: List[int], lo, hi):
        if self.index == len(preorder):
            # we've ran out of the preorder array
            return None

        val = preorder[self.index]
        if not (lo < val < hi):
            # we're in the wrong branch. this value can't be a child in this
            # subtree. do not advance self.index, just move on and let this val
            # be consumed in another subtree
            return None

        self.index += 1
        node = TreeNode(val)
        node.left = self.helper(preorder, lo, val)
        node.right = self.helper(preorder, val, hi)
        return node


def traverse_by_level(root: TreeNode) -> List[Optional[int]]:
    result = []
    front = [root]
    while front:
        new_front = []
        for node in front:
            result.append(node.val if node else None)
            if node and (node.left or node.right):
                new_front.append(node.left)
                new_front.append(node.right)
        front = new_front
        # node, front = front[0], front[1:]
        # result.append(node.val if node else None)
        # if node:
        #     front.append(node.)
    return result


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    # print('input', input_)
    result = Solution().bstFromPreorder(input_)
    # print('tree')
    # print(result)
    result = traverse_by_level(result)
    # print('result', result)
    # print('expected', output)
    assert_eq(result, output)


if __name__ == '__main__':
    test([5, 1, 4, 9], [5, 1, 9, None, 4])
    test([5, 1, 9], [5, 1, 9])
    test([12], [12])
    test([8, 5, 1, 7, 10, 12], [8, 5, 10, 1, 7, None, 12])
