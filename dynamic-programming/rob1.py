"""
House Robber I.

Link: https://leetcode.cn/problems/house-robber/
"""


def rob(nums: list[int]) -> int:
    n = len(nums)
    dp = [[0] * 2 for _ in range(n)]
    dp[0][1] = nums[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = nums[i] + dp[i - 1][0]
    return max(dp[n - 1][0], dp[n - 1][1])
