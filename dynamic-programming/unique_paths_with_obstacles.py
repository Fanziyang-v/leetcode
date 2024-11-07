"""
Unique Paths II.

Link: https://leetcode.cn/problems/unique-paths-ii/
"""


def unique_paths_with_obstacles(obstacles_grid: list[list[int]]) -> int:
    if obstacles_grid[0][0]:
        return 0
    m, n = len(obstacles_grid), len(obstacles_grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    for i in range(1, m):
        if obstacles_grid[i][0]:
            break
        dp[i][0] = 1
    for j in range(1, n):
        if obstacles_grid[0][j]:
            break
        dp[0][j] = 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = 0 if obstacles_grid[i][j] else dp[i][j - 1] + dp[i - 1][j]
    return dp[-1][-1]
