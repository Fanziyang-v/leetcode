"""
Fibonacci Number.

Link: https://leetcode.cn/problems/fibonacci-number/
"""

def fib(n: int) -> int:
    # f(0) = 0, f(1) = 1
    if n in (0, 1):
        return n
    # using rolling array.
    a, b = 0, 1
    for _ in range(n - 1):
        c = a + b
        a, b = b, c
    return c
