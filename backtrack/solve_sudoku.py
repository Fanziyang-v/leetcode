"""
Sudoku Solver.

Link: https://leetcode.cn/problems/sudoku-solver/
"""

N = 9
NUMS = [str(i) for i in range(1, N + 1)]


def isvalid(board: list[list[str]], row: int, col: int, num: str) -> bool:
    # check row and columns
    for i in range(N):
        if board[i][col] == num:
            return False
    for j in range(N):
        if board[row][j] == num:
            return False
    # check sub matrix
    x, y = 3 * (row // 3), 3 * (col // 3)
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if board[i][j] == num:
                return False
    return True


def solve_sudoku(board: list[list[str]]) -> None:

    def backtrack(board: list[list[str]], k: int) -> bool:
        if k == N**2:
            return True
        row, col = k // N, k % N
        if board[row][col].isdigit():
            return backtrack(board, k + 1)
        for num in NUMS:
            if isvalid(board, row, col, num):
                board[row][col] = num
                if backtrack(board, k + 1):
                    return True
                board[row][col] = "."
        return False

    backtrack(board, k=0)
