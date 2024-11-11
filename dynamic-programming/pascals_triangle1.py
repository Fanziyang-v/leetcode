"""
Pascal's Triangle

Link: https://leetcode.cn/problems/pascals-triangle/
"""


def generate(num_rows: int) -> list[list[int]]:
    res = [[1] * (i + 1) for i in range(num_rows)]
    for i in range(2, num_rows):
        for j in range(1, i):
            res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
    return res
