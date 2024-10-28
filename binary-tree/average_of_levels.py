"""
Average of Levels in Binary Tree.

Link: https://leetcode.cn/problems/average-of-levels-in-binary-tree/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode | None'=None, right: 'TreeNode | None'=None):
        self.val = val
        self.left = left
        self.right = right


def average_of_levels(root: TreeNode | None) -> list[float]:
    if root is None:
        return []
    layer = [root]
    res: list[float] = []
    while layer:
        values: list[int] = []
        next_layer: list[TreeNode] = []
        for node in layer:
            values.append(node.val)
            if node.left:
                next_layer.append(node.left)
            if node.right:
                next_layer.append(node.right)
        res.append(sum(values) / len(values))
        layer = next_layer
    return res
