"""
Ugly Number II.

Link: https://leetcode.cn/problems/ugly-number-ii/
"""


def nth_ugly_number(n: int) -> int:
    dp = [0] * (n + 1)
    dp[1] = 1
    p2 = p3 = p5 = 1
    for i in range(2, n + 1):
        dp[i] = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
        if dp[i] == dp[p2] * 2:
            p2 = p2 + 1
        if dp[i] == dp[p3] * 3:
            p3 = p3 + 1
        if dp[i] == dp[p5] * 5:
            p5 = p5 + 1
    return dp[n]
