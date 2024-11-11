"""
Pascal's Triangle II.

Link: https://leetcode.cn/problems/pascals-triangle-ii/
"""


def get_row(row_index: int) -> list[int]:
    if row_index < 2:
        return [1] * (row_index + 1)
    
    dp = [[1] * (row_index + 1) for _ in range(2)]
    prev_index, curr_index = 0, 1
    for i in range(2, row_index + 1):
        for j in range(1, i):
            dp[curr_index][j] = dp[prev_index][j - 1] + dp[prev_index][j]
        prev_index, curr_index = curr_index, prev_index
    return dp[prev_index]
