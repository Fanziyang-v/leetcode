"""
Find First and Last Position of Element in Sorted Array.

Link: https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
"""

def search_left_boundary(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    return left if left < len(nums) and nums[left] == target else -1


def search_right_boundary(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    return left - 1 if left > 0 and nums[left - 1] == target else -1



def search_range(nums: list[int], target: int) -> tuple[int, int]:
    left = search_left_boundary(nums ,target)
    right = search_right_boundary(nums, target)
    return [left, right]
