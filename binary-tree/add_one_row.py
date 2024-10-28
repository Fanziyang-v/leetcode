"""
Add One Row to Tree.

Link: https://leetcode.cn/problems/add-one-row-to-tree/
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


def add_one_row(root: TreeNode, val: int, depth: int) -> TreeNode:
    if depth == 1:
        return TreeNode(val, left=root)

    layer = [root]
    for _ in range(depth - 1):
        next_layer: list[TreeNode] = []
        for node in layer:
            if node.left:
                next_layer.append(node.left)
            if node.right:
                next_layer.append(node.right)
        layer = next_layer

    for node in layer:
        left, right = node.left, node.right
        node.left = TreeNode(val, left=left)
        node.right = TreeNode(val, right=right)
    return root
