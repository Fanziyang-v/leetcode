"""
Binary Search.

Link: https://leetcode.cn/problems/binary-search/
"""
def search(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        elif nums[mid] > target:
            hi = mid - 1
    return -1