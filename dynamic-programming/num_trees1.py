"""
Unique Binary Search Trees.

Link: https://leetcode.cn/problems/unique-binary-search-trees/
"""


def num_trees(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2] = 1, 1, 2
    for i in range(3, n + 1):
        for j in range(i):
            num_left, num_right = j, i - 1 - j
            dp[i] += dp[num_left] * dp[num_right]
    return dp[n]
