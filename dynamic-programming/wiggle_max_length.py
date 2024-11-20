"""
Wiggle Subsequence.

Link: https://leetcode.cn/problems/wiggle-subsequence/
"""


def wiggle_max_length(nums: list[int]) -> int:
    n = len(nums)
    dp = [[1] * 2 for _ in range(n)]
    maxlen = 1
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i][0] = max(1 + dp[j][1], dp[i][0])
            if nums[j] > nums[i]:
                dp[i][1] = max(1 + dp[j][0], dp[i][1])
        maxlen = max(maxlen, dp[i][0], dp[i][1])
    return maxlen
