"""
Search in a Binary Tree.

Link: https://leetcode.cn/problems/search-in-a-binary-search-tree/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode | None'=None, right: 'TreeNode | None'=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root: TreeNode | None, target: int) -> TreeNode | None:
    if root is None:
        return None
    if root.val == target:
        return root
    return searchBST(root.left, target) if root.val > target else searchBST(root.right, target)
