"""
Binary Search Tree Iterator.

Link: https://leetcode.cn/problems/binary-search-tree-iterator/
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


class BSTIterator:
    def __init__(self, root: TreeNode | None) -> None:
        self.data: list[int] = []
        self._traverse(root)

    def next(self) -> int:
        return self.data.pop(0)

    def has_next(self) -> bool:
        return len(self.data) > 0

    def _traverse(self, root: TreeNode | None) -> None:
        if root is None:
            return
        self._traverse(root.left)
        self.data.append(root.val)
        self._traverse(root.right)
