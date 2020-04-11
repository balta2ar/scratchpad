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
    def computePaths(self, root):
        paths = dict()

        def helper(node, path):
            if not node:
                return
            current = path[:] + [node]
            paths[node] = current
            if node.left:
                helper(node.left, current)
            if node.right:
                helper(node.right, current)

        helper(root, [])
        return paths

    def dist(self, path1, path2):
        i1, i2 = 0, 0
        while i1 < len(path1) and i2 < len(path2):
            if path1[i1] == path2[i2]:
                i1, i2 = i1+1, i2+1
            else:
                break
        return len(path1)-i1 + len(path2)-i2

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        paths = list(self.computePaths(root).values())
        #print(paths)
        best = 0
        for i in range(len(paths)):
            for j in range(i+1, len(paths)):
                d = self.dist(paths[i], paths[j])
                #print(d)
                best = max(d, best)
        return best


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
