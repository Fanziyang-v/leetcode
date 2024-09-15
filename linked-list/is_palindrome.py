"""
Palindrome Linked List.

Link: https://leetcode.cn/problems/palindrome-linked-list/
"""
# Definition for a singly-linked list.
class ListNode:
    def __init__(self, val: int=0, next: 'ListNode | None'=None) -> None:
        self.val = val
        self.next = next


def is_palindrome(head: ListNode | None) -> bool:
    if head is None or head.next is None:
        return True
    def is_palindrome_helper(node: ListNode | None) -> bool:
        nonlocal head
        if node is None:
            return True
        if not is_palindrome_helper(node.next) or node.val != head.val:
            return False
        head = head.next
        return True
    return is_palindrome_helper(head)
