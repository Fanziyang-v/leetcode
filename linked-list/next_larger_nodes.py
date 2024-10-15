"""
Next Greater Node in Linked List.

Link: https://leetcode.cn/problems/next-greater-node-in-linked-list/
"""
# Definition for a singly-linked list.
class ListNode:
    def __init__(self, val: int=0, next: 'ListNode | None'=None) -> None:
        self.val = val
        self.next = next


def next_larger_nodes(head: ListNode) -> list[int]:
    values: list[int] = []
    while head:
        values.append(head.val)
        head = head.next
    stack = [values[-1]]
    res = [0] * len(values)
    for i in range(len(values) - 2, -1, -1):
        while stack and stack[-1] <= values[i]:
            stack.pop()
        res[i] = 0 if not stack else stack[-1]
        stack.append(values[i])
    return res
