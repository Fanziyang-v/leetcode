"""
Kth Largest Element in an Array.

Link: https://leetcode.cn/problems/kth-largest-element-in-an-array/
"""
from heapq import heapify, heapreplace

def find_kth_largest(nums: list[int], k: int) -> int:
    min_heap = nums[:k]
    heapify(min_heap)
    for num in nums[k:]:
        if num > min_heap[0]:
            heapreplace(min_heap, num)
    return min_heap[0]
