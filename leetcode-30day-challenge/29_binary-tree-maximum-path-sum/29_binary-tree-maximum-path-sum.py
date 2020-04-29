from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    best = None
    def maxPathSum(self, root: TreeNode) -> int:
        import sys
        self.best = -sys.maxsize
        self.helper(root)
        return self.best

    def helper(self, node: TreeNode) -> int:
        if node == None: return 0
        left = max(0, self.helper(node.left))
        right = max(0, self.helper(node.right))
        self.best = max(self.best, node.val + left + right)
        return node.val + max(left, right)


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input1, output):
    result = Solution().maxPathSum(input1)
    assert_eq(result, output)


if __name__ == '__main__':
    tree = TreeNode(-3, None, None)
    test(tree, -3)

    tree = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
    test(tree, 6)

    tree = TreeNode(
        -10,
        TreeNode(9, None, None),
        TreeNode(
            20,
            TreeNode(15, None, None),
            TreeNode(7, None, None)
        )
    )
    test(tree, 42)
