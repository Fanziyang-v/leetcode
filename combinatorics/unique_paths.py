"""
Unique Paths.

Link: https://leetcode.cn/problems/unique-paths/
"""


def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    prod = 1
    for i in range(2, n + 1):
        prod *= i
    return prod


def unique_paths(m: int, n: int) -> int:
    return int(factorial(m + n - 2) / (factorial(m - 1) * factorial(n - 1)))
