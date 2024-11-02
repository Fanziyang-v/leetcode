"""
Remove Zero Sum Consecutive Nodes from Linked List.

Link: https://leetcode.cn/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
"""


# Definition for a singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def remove_zero_sum_sublists(head: ListNode | None) -> ListNode | None:
    prefix_sum2node: dict[int, ListNode] = {}
    curr = dummy = ListNode(val=0, next=head)
    prefix_sum = 0
    while curr:
        prefix_sum += curr.val
        prefix_sum2node[prefix_sum] = curr
        curr = curr.next

    prefix_sum = 0
    curr = dummy
    while curr:
        prefix_sum += curr.val
        curr.next = prefix_sum2node[prefix_sum].next
        curr = curr.next
    return dummy.next
