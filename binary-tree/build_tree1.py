"""
Construct Binary Tree from Preorder and Inorder Traversal.

Link: https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode | None'=None, right: 'TreeNode | None'=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    if not preorder:
        return None
    rootval = preorder[0]
    root = TreeNode(rootval)
    pos = inorder.index(rootval)
    root.left = build_tree(preorder[1:pos+1], inorder[:pos])
    root.right = build_tree(preorder[pos+1:], inorder[pos+1:])
    return root
