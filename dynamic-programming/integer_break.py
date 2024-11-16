"""
Integer Break.

Link: https://leetcode.cn/problems/integer-break/
"""


def integer_break(n: int) -> int:
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        for j in range(1, i // 2 + 1):
            dp[i] = max(
                dp[i], dp[i - j] * dp[j], (i - j) * dp[j], dp[i - j] * j, (i - j) * j
            )
    return dp[n]
