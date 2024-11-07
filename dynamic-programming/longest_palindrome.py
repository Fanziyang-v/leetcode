"""
Longest Palindromic Substring.

Link: https://leetcode.cn/problems/longest-palindromic-substring/
"""


def longest_palindrome(s: str) -> str:
    n = len(s)
    if n < 2:
        return s
    dp = [[False] * n for _ in range(n)]
    res = s[0]
    maxlen = 1
    for i in range(n):
        dp[i][i] = True
        if i + 1 < n:
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                res = s[i : i + 2]
                maxlen = 2
    for k in range(2, n):
        row, col = 0, k
        while row < n and col < n:
            dp[row][col] = dp[row + 1][col - 1] and s[row] == s[col]
            if dp[row][col]:
                length = col - row + 1
                if maxlen < length:
                    maxlen = length
                    res = s[row : col + 1]
            row, col = row + 1, col + 1
    return res
