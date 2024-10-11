"""
Convert a Binary Number in a Linked List to Integer.

Link: https://leetcode.cn/problems/convert-binary-number-in-a-linked-list-to-integer/
"""
# Definition for a singly-linked list.
class ListNode:
    def __init__(self, val: int=0, next: 'ListNode | None'=None) -> None:
        self.val = val
        self.next = next

RADIX = 2
def get_decimal_value(head: ListNode) -> int:
    value = 0
    while head:
        value = value * RADIX + head.val
        head = head.next
    return value
