"""
The K Weakest Rows in a Matrix.

Link: https://leetcode.cn/problems/the-k-weakest-rows-in-a-matrix/
"""

from heapq import heapify, heappop


def k_weakest_rows(mat: list[list[int]], k: int) -> list[int]:
    m, n = len(mat), len(mat[0])
    powers: list[tuple[int]] = []
    for i in range(m):
        lo, hi = 0, n
        power = -1
        while lo < hi:
            mid = (lo + hi) // 2
            if mat[i][mid] == 0:
                hi = mid
            else:
                lo = mid + 1
                power = mid
        powers.append((power + 1, i))
    heapify(powers)
    return [heappop(powers)[1] for _ in range(k)]
