"""
Kth Largest Element in a Stream.

Link: https://leetcode.cn/problems/kth-largest-element-in-a-stream/
"""

from heapq import heapify, heapreplace, heappush


class KthLargest:
    def __init__(self, k: int, nums: list[int]) -> None:
        self.capacity = k
        self.min_heap = nums[:k]
        heapify(self.min_heap)
        for num in nums[k:]:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.capacity:
            heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapreplace(self.min_heap, val)
        return self.min_heap[0]
