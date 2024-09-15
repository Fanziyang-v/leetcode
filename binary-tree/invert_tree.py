"""
Invert Binary Tree.

Link: https://leetcode.cn/problems/invert-binary-tree/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode | None'=None, right: 'TreeNode | None'=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    if root is None:
        return None
    left = invert_tree(root.left)
    right = invert_tree(root.right)
    root.left, root.right = right, left
    return root
