"""
Path Sum Ⅱ

Link: https://leetcode.cn/problems/path-sum-ii/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode | None'=None, right: 'TreeNode | None'=None):
        self.val = val
        self.left = left
        self.right = right


def isleaf(node: TreeNode) -> bool:
    return node.left is None and node.right is None


def path_sum(root: TreeNode | None, target_sum: int) -> list[list[int]]:
    res: list[list[int]] = []
    def traverse(root: TreeNode | None, target: int, track: list[int]=[]) -> None:
        nonlocal res
        if root is None:
            return
        track.append(root.val)
        if isleaf(root) and root.val == target:
            res.append(track[:])
            track.pop()
            return
        
        traverse(root.left, target - root.val, track)
        traverse(root.right, target - root.val, track)
        track.pop()
    traverse(root, target_sum)
    return res
