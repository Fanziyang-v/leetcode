"""
Split Linked List in Parts.

Link: https://leetcode.cn/problems/split-linked-list-in-parts/
"""


# Definition for a singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def list_length(head: ListNode | None) -> int:
    length = 0
    while head:
        length += 1
        head = head.next
    return length


def split_list_to_parts(head: ListNode | None, k: int) -> list[ListNode | None]:
    length = list_length(head)
    n, m = length // k, length % k
    res: list[ListNode | None] = []
    curr = head
    for i in range(k):
        res.append(curr)
        sublist_length = n + 1 if i < m else n
        for _ in range(sublist_length - 1):
            if curr:
                curr = curr.next
        if curr:
            temp = curr.next
            curr.next = None
            curr = temp
    return res
