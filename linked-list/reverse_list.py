"""
Reverse Linked List.

Link: https://leetcode.cn/problems/reverse-linked-list/
"""
# Definition for a singly-linked list.
class ListNode:
    def __init__(self, val: int=0, next: 'ListNode | None'=None) -> None:
        self.val = val
        self.next = next


# Recursive version.
def reverse_list(head: ListNode | None) -> ListNode | None:
    if head is None or head.next is None:
        return head
    last = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return last


# Iterative version.
def reverse_list1(head: ListNode | None) -> ListNode | None:
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev, curr = curr, temp
    return prev
