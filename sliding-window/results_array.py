"""
Find the Power of K-Size Subarray I.

Link: https://leetcode.cn/problems/find-the-power-of-k-size-subarrays-i/
"""


def is_sorted(nums: list[int]) -> bool:
    if len(nums) <= 1:
        return True
    for i in range(len(nums) - 1):
        if nums[i + 1] <= nums[i]:
            return False
    return True


def results_array(nums: list[int], k: int) -> list[int]:
    res = [-1] * (len(nums) - k + 1)
    for i in range(k - 1, len(nums)):
        res[i - k + 1] = nums[i] if is_sorted(nums[i - k + 1 : i + 1]) else -1
    return res
