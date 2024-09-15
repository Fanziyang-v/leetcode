"""
Flatten Binary Tree To Linked List.

Link: https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode | None'=None, right: 'TreeNode | None'=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root: TreeNode | None) -> None:
    if root is None:
        return
    flatten(root.left)
    flatten(root.right)
    if root.left is None:
        return
    if root.right:
        curr = root.left
        while curr.right:
            curr = curr.right
        curr.right = root.right
    root.right = root.left
    root.left = None
