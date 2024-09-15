"""
Minimum Depth of Binary Tree.

Link: https://leetcode.cn/problems/minimum-depth-of-binary-tree/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode | None'=None, right: 'TreeNode | None'=None):
        self.val = val
        self.left = left
        self.right = right


def isleaf(node: TreeNode) -> bool:
    return node.left is None and node.right is None


def min_depth(root: TreeNode | None) -> int:
    if root is None:
        return 0
    layer = [root]
    depth = 0
    while layer:
        depth += 1
        next_layer: list[TreeNode] = []
        for node in layer:
            if isleaf(node):
                return depth
            if node.left:
                next_layer.append(node.left)
            if node.right:
                next_layer.append(node.right)
        layer = next_layer
    raise AssertionError # Never Happen
