"""
Symmetric Tree.

Link: https://leetcode.cn/problems/symmetric-tree/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode | None'=None, right: 'TreeNode | None'=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: TreeNode | None) -> bool:
    if root is None:
        return True
    def is_symmetric_helper(p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True
        elif p and q:
            return p.val == q.val and is_symmetric_helper(p.left, q.right) and is_symmetric_helper(p.right, q.left)
        return False
    return is_symmetric_helper(root.left, root.right)
