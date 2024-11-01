"""
Most Frequent Subtree Sum.

Link: https://leetcode.cn/problems/most-frequent-subtree-sum/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


def isleaf(node: TreeNode | None) -> bool:
    return node.left is None and node.right is None


def find_frequent_tree_sum(root: TreeNode) -> list[int]:
    total2freq: dict[int, int] = {}

    def dfs(node: TreeNode | None) -> int:
        if node is None:
            return 0
        total = node.val + dfs(node.left) + dfs(node.right)
        total2freq[total] = total2freq.get(total, 0) + 1
        return total

    dfs(root)
    maxfreq = max(total2freq.values())
    return [total for total, freq in total2freq.items() if freq == maxfreq]
