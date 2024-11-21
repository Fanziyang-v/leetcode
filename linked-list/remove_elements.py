"""
Remove Linked List Elements.

Link: https://leetcode.cn/problems/remove-linked-list-elements/
"""


# Definition for a singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def remove_elements(head: ListNode | None, val: int) -> ListNode | None:
    curr = dummy = ListNode(next=head)
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next
