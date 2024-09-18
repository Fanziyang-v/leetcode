"""
Kth Smallest Element in a BST.

Link: https://leetcode.cn/problems/kth-smallest-element-in-a-bst/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode | None'=None, right: 'TreeNode | None'=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: TreeNode | None, k: int) -> int:
    res = -1
    i = 0
    def traverse(root: TreeNode | None) -> None:
        nonlocal i, res
        if root is None or i == k:
            return
        traverse(root.left)
        i += 1
        if i == k:
            res = root.val
            return
        traverse(root.right)
    traverse(root)
    return res
