"""
Convert Sorted List to Binary Search Tree.

Link: https://leetcode.cn/problems/convert-sorted-list-to-binary-search-tree/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode | None'=None, right: 'TreeNode | None'=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for singly-linked list
class ListNode:
    def __init__(self, val: int=0, next: 'ListNode | None'=None) -> None:
        self.val = val
        self.next = next


def sorted_list2BST(head: ListNode | None, tail: ListNode | None=None) -> TreeNode | None:
    if head == tail:
        return None
    def middle_node(head: ListNode, tail: ListNode | None) -> ListNode:
        slow = fast = head
        while fast != tail and fast.next != tail:
            slow, fast = slow.next, fast.next.next
        return slow
    mid_node = middle_node(head, tail)
    root = TreeNode(mid_node.val)
    root.left = sorted_list2BST(head, mid_node)
    root.right = sorted_list2BST(mid_node.next, tail)
    return root
