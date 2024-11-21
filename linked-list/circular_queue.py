"""
Design Circular Queue.

Link: https://leetcode.cn/problems/design-circular-queue/
"""


# Definition for a singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class CircularQueue:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.size = 0
        self.rear: ListNode | None = None

    def enqueue(self, value: int) -> bool:
        if self.is_full():
            return False
        if self.is_empty():
            self.rear = ListNode(value)
            self.rear.next = self.rear
        else:
            front = self.rear.next
            self.rear.next = ListNode(value, next=front)
            self.rear = self.rear.next
        self.size += 1
        return True

    def dequeue(self) -> bool:
        if self.is_empty():
            return False
        front = self.rear.next
        if front == self.rear:
            self.rear = None
        else:
            self.rear.next = front.next
        self.size -= 1
        return True

    def get_front(self) -> int:
        return -1 if self.is_empty() else self.rear.next.val

    def get_rear(self) -> int:
        return -1 if self.is_empty() else self.rear.val

    def is_empty(self) -> bool:
        return self.rear is None

    def is_full(self) -> bool:
        return self.size == self.capacity
