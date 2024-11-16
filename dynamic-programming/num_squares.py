"""
Perfect Squares.

Link: https://leetcode.cn/problems/perfect-squares/
"""


def num_sqaures(n: int) -> int:
    dp = [i for i in range(n + 1)]
    for i in range(1, n + 1):
        num = 1
        while i - num**2 >= 0:
            dp[i] = min(dp[i], dp[i - num**2] + 1)
            num = num + 1
    return dp[n]
