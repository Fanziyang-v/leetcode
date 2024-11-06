"""
Maximum Subarray.

Link: https://leetcode.cn/problems/maximum-subarray/
"""


def max_sub_array(nums: list[int]) -> int:
    dp: list[int] = [0] * len(nums)
    res = dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], nums[i] + dp[i - 1])
        res = max(res, dp[i])
    return res
