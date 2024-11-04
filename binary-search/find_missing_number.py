"""
Missing Number.

Link: https://leetcode.cn/problems/missing-number/
"""


def find_missing_number(nums: list[int]) -> int:
    sorted_nums = sorted(nums)
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if sorted_nums[mid] == mid:
            lo = mid + 1
        elif sorted_nums[mid] > mid:
            hi = mid
    return lo
