from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        return self.helper(root, arr, 0)
    def helper(self, node, arr, index):
        if not arr: return False
        if node is None: return False
        if index == len(arr)-1: # last one?
            is_leaf = node.left is None and node.right is None
            return is_leaf and node.val == arr[index]
        if arr[index] != node.val: return False
        left = self.helper(node.left, arr, index+1)
        right = self.helper(node.right, arr, index+1)
        return left or right


def assert_eq(actual, expected):
    if actual != expected:
        raise AssertionError('expected: %s, actual: %s' % (expected, actual))


def test(tree, arr, output):
    result = Solution().isValidSequence(tree, arr)
    assert_eq(result, output)


if __name__ == '__main__':
    tree = TreeNode(
        8,
        TreeNode(
            3,
            TreeNode(1, None, None),
            None,
        ),
        TreeNode(
            2,
            TreeNode(5, None, None),
            TreeNode(4, None, None),
        )
    )
    test(tree, [8], False)

    # [8,3,null,2,1,5,4]
    # [8]
    tree = TreeNode(
        8,
        TreeNode(
            3,
            TreeNode(1, None, None),
            TreeNode(2, None, None),
        ),
        None,
    )
    test(tree, [8], False)


    tree = TreeNode(
        0,
        TreeNode(
            1,
            TreeNode(
                0,
                None,
                TreeNode(1, None, None)
            ),
            TreeNode(
                1,
                TreeNode(0, None, None),
                TreeNode(0, None, None),
            ),
        ),
        TreeNode(
            0,
            TreeNode(0, None, None),
            None,
        )
    )
    test(tree, [0, 1, 0, 1], True)
    test(tree, [0, 1, 1, 0], True)
    test(tree, [0, 1, 1, 0], True)
    #test(tree, [0, 1, 1], True)
    # arr can be found in the tree, but it doesn't end at a leaf
    test(tree, [0, 1, 1], False)

    test(tree, [0, 0, 1], False)
    test(tree, [0, 1, 1], False)
