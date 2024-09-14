"""
Binary Tree Preorder Traversal.

Link: https://leetcode.cn/problems/binary-tree-preorder-traversal/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode | None'=None, right: 'TreeNode | None'=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive version.
def preorder_traversal(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)


# Iterative version.
def preorder_traversal1(root: TreeNode | None) -> list[int]:
    res: list[int] = []
    stack: list[TreeNode] = []
    curr = root
    while curr or stack:
        if curr:
            res.append(curr.val)
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            curr = curr.right
    return res
