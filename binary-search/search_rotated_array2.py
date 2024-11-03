"""
Search in Rotated Sorted Array Ⅱ.

Link: https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/
"""


def search_rotated_array(nums: list[int], target: int) -> bool:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return True
        if nums[lo] == nums[mid] and nums[mid] == nums[hi]:
            lo, hi = lo + 1, hi - 1
        elif nums[mid] >= nums[lo]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return False
