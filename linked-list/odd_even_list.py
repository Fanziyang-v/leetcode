"""
Odd Even Linked List.

Link: https://leetcode.cn/problems/odd-even-linked-list/
"""
# Definition for a singly-linked list.
class ListNode:
    def __init__(self, val: int=0, next: 'ListNode | None'=None) -> None:
        self.val = val
        self.next = next


def odd_even_list(head: ListNode | None) -> ListNode | None:
    if head is None or head.next is None:
        return head
    dummy1, dummy2 = ListNode(-1), ListNode(-1)
    p, q = dummy1, dummy2
    index = 0
    while head:
        index += 1
        if index % 2 == 1:
            p.next = head
            p = p.next
        else:
            q.next = head
            q = q.next
        head = head.next
    p.next, q.next = dummy2.next, None
    return dummy1.next
