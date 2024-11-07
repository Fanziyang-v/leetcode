"""
Jump Game II.

Link: https://leetcode.cn/problems/jump-game-ii/
"""


def jump(nums: list[int]) -> int:
    n = len(nums)
    INFINITY = float("+inf")
    dp = [INFINITY] * n
    dp[-1] = 0
    for i in range(n - 2, -1, -1):
        if nums[i] > 0:
            dp[i] = min(dp[i + 1 : i + nums[i] + 1]) + 1
    return dp[0]
