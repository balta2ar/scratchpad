from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)


class Solution:
    max = 0
    def diameterOfBinaryTree(self, node: TreeNode) -> int:
        self.max = 0
        self.maxDepth(node)
        return self.max

    def maxDepth(self, node):
        if not node:
            return 0

        left = self.maxDepth(node.left)
        right = self.maxDepth(node.right)
        self.max = max(self.max, left+right)
        return max(left, right) + 1


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(input_, output):
    assert_eq(Solution().diameterOfBinaryTree(input_), output)


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    test(tree, 2)

    test(None, 0)

    tree = TreeNode(1)
    test(tree, 0)

    tree = TreeNode(1)
    tree.left = TreeNode(2)
    test(tree, 1)
