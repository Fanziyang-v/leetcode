"""
Find Largest Values in Each Tree Row.

Link: https://leetcode.cn/problems/find-largest-value-in-each-tree-row/
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


def largest_values(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    res = []
    layer = [root]
    while layer:
        next_layer = []
        values = []
        for node in layer:
            values.append(node.val)
            if node.left:
                next_layer.append(node.left)
            if node.right:
                next_layer.append(node.right)
        res.append(max(values))
        layer = next_layer
    return res
