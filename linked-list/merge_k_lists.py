"""
Merge K Sorted Lists.

Link: https://leetcode.cn/problems/merge-k-sorted-lists/
"""


# Definition for a singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    r = dummy = ListNode()
    p, q = list1, list2
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


def merge_k_lists(lists: list[ListNode | None]) -> ListNode | None:
    if not lists:
        return None
    n = len(lists)
    if n == 1:
        return lists[0]
    elif n == 2:
        return merge_two_lists(lists[0], lists[1])

    left = merge_k_lists(lists[: n // 2])
    right = merge_k_lists(lists[n // 2 :])
    return merge_two_lists(left, right)
