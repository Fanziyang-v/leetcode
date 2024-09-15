"""
Merge Two Sorted Lists.

Link: https://leetcode.cn/problems/merge-two-sorted-lists/
"""
# Definition for a singly-linked list.
class ListNode:
    def __init__(self, val: int=0, next: 'ListNode | None'=None) -> None:
        self.val = val
        self.next = next


# Recursive version.
def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    if list1.val <= list2.val:
        list1.next = merge_two_lists(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists(list1, list2.next)
        return list2


# Iterative version.
def merge_two_lists1(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    dummy = ListNode() # dummy node
    p, q, r = list1, list2, dummy

    while p and q:
        if p.val <= q.val:
            r.next = p
            p = p.next
        else:
            r.next = q
            q = q.next
        r = r.next
    r.next = p if p else q
    return dummy.next
