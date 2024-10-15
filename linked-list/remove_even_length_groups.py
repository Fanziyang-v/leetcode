"""
Remove Nodes in Even Length Groups.

Link: https://leetcode.cn/problems/reverse-nodes-in-even-length-groups/
"""
# Definition for a singly-linked list.
class ListNode:
    def __init__(self, val: int=0, next: 'ListNode | None'=None) -> None:
        self.val = val
        self.next = next


def reverse(head: ListNode, tail: ListNode | None) -> ListNode:
    prev, curr = tail, head
    while curr != tail:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def reverse_even_length_groups(head: ListNode) -> ListNode:
    n = 1
    prev_last, curr = None, head
    while curr:
        curr_last = None
        start = end = curr
        length = 0
        while end and length < n:
            curr_last = end
            end = end.next
            length += 1
        if length % 2 == 0:
            prev_last.next = reverse(start, end)
            prev_last = start
        else:
            prev_last = curr_last
        curr = end
        n += 1
    return head
