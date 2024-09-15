"""
Delete Node in a BST.

Link: https://leetcode.cn/problems/delete-node-in-a-bst/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode | None'=None, right: 'TreeNode | None'=None):
        self.val = val
        self.left = left
        self.right = right


def delete_node(root: TreeNode | None, key: int) -> TreeNode | None:
    if root is None:
        return None
    if root.val > key:
        root.left = delete_node(root.left, key)
    elif root.val < key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        curr = root.left
        while curr.right:
            curr = curr.right
        root.val = curr.val
        root.left = delete_node(root.left, root.val)
    return root
