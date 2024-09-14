"""
Construct Binary Tree from Inorder and Postorder Traversal.

Link: https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode | None'=None, right: 'TreeNode | None'=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(inorder: list[int], postorder: list[int]) -> TreeNode | None:
    if not inorder:
        return None
    rootval = postorder[-1]
    root = TreeNode(rootval)
    pos = inorder.index(rootval)
    root.left = build_tree(inorder[:pos], postorder[:pos])
    root.right = build_tree(inorder[pos+1:], postorder[pos+1:-1])
    return root
