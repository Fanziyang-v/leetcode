"""
N-Queens.

Link: https://leetcode.cn/problems/n-queens/
"""


def isvalid(board: list[list[str]], row: int, col: int, n: int) -> bool:
    for i in range(row):
        if board[i][col] == "Q":
            return False
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i, j = i - 1, j + 1
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i, j = i - 1, j - 1
    return True


def solve_n_queens(n: int) -> list[list[str]]:
    res: list[list[str]] = []
    board = [["."] * n for _ in range(n)]

    def backtrack(board: list[list[str]], i: int) -> None:
        nonlocal res
        if i == n:
            solution = ["".join(line) for line in board]
            res.append(solution)
            return
        for j in range(n):
            if isvalid(board, i, j, n):
                board[i][j] = "Q"
                backtrack(board, i + 1)
                board[i][j] = "."

    backtrack(board, 0)
    return res
