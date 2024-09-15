"""
Validate Binary Search Tree.

Link: https://leetcode.cn/problems/validate-binary-search-tree/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode | None'=None, right: 'TreeNode | None'=None):
        self.val = val
        self.left = left
        self.right = right


def is_validBST(root: TreeNode | None, 
                minval: float=float('-inf'),
                maxval: float=float('inf')) -> bool:
    if root is None:
        return True
    return minval < root.val < maxval \
        and is_validBST(root.left, minval, root.val) \
            and is_validBST(root.right, root.val, maxval)
