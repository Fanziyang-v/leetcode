"""
Binary Tree Right Side View.

Link: https://leetcode.cn/problems/binary-tree-right-side-view/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode | None'=None, right: 'TreeNode | None'=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    layer = [root]
    res: list[int] = []
    while layer:
        res.append(layer[-1].val)
        next_layer: list[TreeNode] = []
        for node in layer:
            if node.left:
                next_layer.append(node.left)
            if node.right:
                next_layer.append(node.right)
        layer = next_layer
    return res
