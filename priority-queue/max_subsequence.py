"""
Find Subsequence of Length K With the Largest Sum.

Link: https://leetcode.cn/problems/find-subsequence-of-length-k-with-the-largest-sum/
"""

from heapq import heapify, heapreplace


def max_subsequence(nums: list[int], k: int) -> list[int]:
    min_heap = [(nums[i], i) for i in range(k)]
    heapify(min_heap)
    for i in range(k, len(nums)):
        if nums[i] > min_heap[0][0]:
            heapreplace(min_heap, (nums[i], i))
    indices = [index for _, index in min_heap]
    indices.sort()
    return [nums[idx] for idx in indices]
