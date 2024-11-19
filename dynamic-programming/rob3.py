"""
House Robber III.

Link: https://leetcode.cn/problems/house-robber-iii/
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


def rob(root: TreeNode) -> int:
    def rob_helper(root: TreeNode | None) -> tuple[int, int]:
        if root is None:
            return 0, 0
        a1, b1 = rob_helper(root.left)
        a2, b2 = rob_helper(root.right)
        return max(a1, b1) + max(a2, b2), a1 + a2 + root.val

    return max(rob_helper(root))
