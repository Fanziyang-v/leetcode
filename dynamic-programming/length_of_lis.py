"""
Longest Increasing Subsequence.

Link: https://leetcode.cn/problems/longest-increasing-subsequence/
"""


def length_of_LIS(nums: list[int]) -> int:
    n = len(nums)
    dp = [1] * n
    maxlen = 1
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
        maxlen = max(maxlen, dp[i])
    return maxlen
