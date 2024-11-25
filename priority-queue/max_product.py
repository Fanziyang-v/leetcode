"""
Maximum Product of Two Elements in an Array.

Link: https://leetcode.cn/problems/maximum-product-of-two-elements-in-an-array/
"""

from heapq import heapify, heapreplace


def max_product(nums: list[int]) -> int:
    min_heap = nums[:2]
    heapify(min_heap)
    for num in nums[2:]:
        if num > min_heap[0]:
            heapreplace(min_heap, num)
    return (min_heap[0] - 1) * (min_heap[1] - 1)
