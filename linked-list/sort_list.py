"""
Sort List.

Link: https://leetcode.cn/problems/sort-list/
"""
# Definition for a singly-linked list.
class ListNode:
    def __init__(self, val: int=0, next: 'ListNode | None'=None) -> None:
        self.val = val
        self.next = next


def sort_list(head: ListNode | None, tail: ListNode | None=None) -> ListNode | None:
    if head == tail:
        return None
    if head.next == tail:
        head.next = None
        return head
    mid_node = find_middle_node(head, tail)
    left = sort_list(head, mid_node)
    right = sort_list(mid_node, tail)
    return merge_two_lists(left, right)


def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    dummy = ListNode(-1)
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


def find_middle_node(head: ListNode, tail: ListNode | None) -> ListNode:
    slow = fast = head
    while fast != tail and fast.next != tail:
        slow, fast = slow.next, fast.next.next
    return slow
