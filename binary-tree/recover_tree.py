"""
Recover Binary Search Tree.

Link: https://leetcode.cn/problems/recover-binary-search-tree/
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


def recover_tree(root: TreeNode | None) -> None:
    p: TreeNode | None = None
    q: TreeNode | None = None
    prev: TreeNode | None = None

    def traverse(node: TreeNode | None) -> None:
        nonlocal p, q, prev
        if node is None:
            return
        traverse(node.left)
        if prev and prev.val > node.val:
            p = p if p else prev
            q = node
        prev = node
        traverse(node.right)

    traverse(root)
    p.val, q.val = q.val, p.val
