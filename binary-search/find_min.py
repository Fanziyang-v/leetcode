"""
Find Minimum in Rotated Sorted Array.

Link: https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/
"""


def find_min(nums: list[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] >= nums[0]:
            lo = mid + 1
        elif nums[mid] < nums[0]:
            hi = mid - 1
    return nums[lo % len(nums)]
