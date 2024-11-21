"""
Insert Greatest Common Divisors in Linked List.

Link: https://leetcode.cn/problems/insert-greatest-common-divisors-in-linked-list/
"""


# Definition for a singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def gcd(a: int, b: int) -> int:
    a, b = max(a, b), min(a, b)
    while b:
        a, b = b, a % b
    return a


def insert_greatest_common_divisors(head: ListNode) -> ListNode | None:
    curr = head
    while curr and curr.next:
        new_node = ListNode(val=gcd(curr.val, curr.next.val), next=curr.next)
        curr.next = new_node
        curr = new_node.next
    return head
