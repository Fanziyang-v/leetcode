"""
Path Sum

Link: https://leetcode.cn/problems/path-sum/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode | None'=None, right: 'TreeNode | None'=None):
        self.val = val
        self.left = left
        self.right = right


def isleaf(root: TreeNode) -> bool:
    return root.left is None and root.right is None


def has_path_sum(root: TreeNode | None, target_sum: int) -> bool:
    if root is None:
        return False
    if isleaf(root) and root.val == target_sum:
        return True
    return has_path_sum(root.left, target_sum - root.val) \
        or has_path_sum(root.right, target_sum - root.val)
