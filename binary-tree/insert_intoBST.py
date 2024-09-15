"""
Insert into a Binary Search Tree.

Link: https://leetcode.cn/problems/insert-into-a-binary-search-tree/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode | None'=None, right: 'TreeNode | None'=None):
        self.val = val
        self.left = left
        self.right = right


def insert_intoBST(root: TreeNode | None, val: int) -> TreeNode:
    if root is None:
        return TreeNode(val)
    # Already exists val.
    if root.val == val:
        return root
    if root.val > val:
        root.left = insert_intoBST(root.left, val)
    if root.val < val:
        root.right = insert_intoBST(root.right, val)
    return root
