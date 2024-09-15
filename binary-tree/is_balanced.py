"""
Balanced Binary Tree.

Link: https://leetcode.cn/problems/balanced-binary-tree/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode | None'=None, right: 'TreeNode | None'=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root: TreeNode | None) -> bool:
    def is_balanced_helper(root: TreeNode | None) -> int:
        if root is None:
            return 0
        left_height = is_balanced_helper(root.left)
        if left_height < 0:
            return -1
        right_height = is_balanced_helper(root.right)
        if right_height < 0:
            return -1
        return -1 if abs(left_height - right_height) > 1 else 1 + max(left_height, right_height)
    return is_balanced_helper(root) >= 0
