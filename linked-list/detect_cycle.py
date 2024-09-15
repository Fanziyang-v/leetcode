"""
Linked List CycleⅡ

Link: https://leetcode.cn/problems/linked-list-cycle-ii/
"""
# Definition for a singly-linked list.
class ListNode:
    def __init__(self, val: int=0, next: 'ListNode | None'=None) -> None:
        self.val = val
        self.next = next


def detect_cycle(head: ListNode | None) -> ListNode | None:
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            break
    # No cycle.
    if fast is None or fast.next is None:
        return None
    slow = head
    while slow != fast:
        slow, fast = slow.next, fast.next
    return slow
