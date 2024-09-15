"""
Remove Duplicates from Sorted List.

Link: https://leetcode.cn/problems/remove-duplicates-from-sorted-list/
"""
# Definition for a singly-linked list.
class ListNode:
    def __init__(self, val: int=0, next: 'ListNode | None'=None) -> None:
        self.val = val
        self.next = next


def remove_duplicates(head: ListNode | None) -> ListNode | None:
    if head is None or head.next is None:
        return head
    p = head
    while p and p.next:
        q = p.next
        while q and q.val == p.val:
            q = q.next
        p.next = q
        p = p.next
    return head
