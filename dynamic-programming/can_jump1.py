"""
Jump Game.

Link: https://leetcode.cn/problems/jump-game/
"""


def can_jump(nums: list[int]) -> bool:
    n = len(nums)
    dp = [False] * n
    dp[-1] = True
    for i in range(n - 2, -1, -1):
        dp[i] = True if nums[i] + i >= n - 1 else any(dp[i + 1 : i + nums[i] + 1])
    print(dp)
    return dp[0]
