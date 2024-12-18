"""
Coin Change.

Link: https://leetcode.cn/problems/coin-change/
"""


def coin_change(coins: list[int], amount: int) -> int:
    dp = [float("+inf")] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return -1 if dp[amount] == float("+inf") else dp[amount]
