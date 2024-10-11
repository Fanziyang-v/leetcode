"""
Intersection of Two Linked Lists.

Link: https://leetcode.cn/problems/intersection-of-two-linked-lists/
"""
# Definition for a singly-linked list.
class ListNode:
    def __init__(self, val: int=0, next: 'ListNode | None'=None) -> None:
        self.val = val
        self.next = next


def get_intersection_node(headA: ListNode, headB: ListNode) -> 'ListNode | None':
    p, q = headA, headB
    while p != q:
        p = p.next if p is not None else headB
        q = q.next if q is not None else headA
    return p
