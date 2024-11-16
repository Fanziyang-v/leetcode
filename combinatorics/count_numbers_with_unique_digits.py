"""
Count Numbers with Unique Digits.

Link: https://leetcode.cn/problems/count-numbers-with-unique-digits/
"""


def count_numbers_with_unique_digits(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 10
    res, curr = 10, 9
    for i in range(n - 1):
        curr *= 9 - i
        res += curr
    return res
