"""
Construct Sorted Array to Binary Search Tree.

Link: https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode | None'=None, right: 'TreeNode | None'=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_array2BST(nums: list[int]) -> TreeNode | None:
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array2BST(nums[:mid])
    root.right = sorted_array2BST(nums[mid+1:])
    return root
