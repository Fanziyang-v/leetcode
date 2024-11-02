"""
Path Sum Ⅲ

Link: https://leetcode.cn/problems/path-sum-iii/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def path_sum_helper(root: TreeNode | None, target_sum: int) -> int:
    if root is None:
        return 0
    left = path_sum_helper(root.left, target_sum - root.val)
    right = path_sum_helper(root.right, target_sum - root.val)
    return left + right + (1 if root.val == target_sum else 0)


def path_sum(root: TreeNode | None, target_sum: int) -> int:
    if root is None:
        return 0
    return (
        path_sum_helper(root, target_sum)
        + path_sum(root.left, target_sum)
        + path_sum(root.right, target_sum)
    )
