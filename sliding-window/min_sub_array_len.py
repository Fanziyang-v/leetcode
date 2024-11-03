"""
Minimum Size Subarray Sum.

Link: https://leetcode.cn/problems/minimum-size-subarray-sum/
"""


def min_sub_array_sum(nums: list[int], target: int) -> int:
    n = len(nums)
    left = right = 0
    wsum = 0
    min_len = float("+inf")
    while right < n:
        # expand window
        wsum += nums[right]
        right += 1
        # shrink window
        while left < right and wsum >= target:
            min_len = min(min_len, right - left)
            wsum -= nums[left]
            left += 1
    return min_len if min_len < float("+inf") else 0
