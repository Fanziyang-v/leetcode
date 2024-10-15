"""
Delete the Middle Node of a Linked List.

Link: https://leetcode.cn/problems/delete-the-middle-node-of-a-linked-list/
"""
# Definition for a singly-linked list.
class ListNode:
    def __init__(self, val: int=0, next: 'ListNode | None'=None) -> None:
        self.val = val
        self.next = next


def delete_middle(head: ListNode) -> ListNode | None:
    if head.next is None:
        return None
    prev = None
    slow = fast = head
    while fast and fast.next:
        prev = slow
        slow, fast = slow.next, fast.next.next
    prev.next = prev.next.next
    return head
