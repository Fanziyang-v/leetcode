"""
Beautiful Arrangement.

Link: https://leetcode.cn/problems/beautiful-arrangement/
"""


def count_arrangement(n: int) -> int:
    res = 0

    def backtrack(track: list[int] = []) -> None:
        nonlocal res
        if len(track) == n:
            res += 1
            return
        for i in range(1, n + 1):
            if i not in track and (
                i % (len(track) + 1) == 0 or (len(track) + 1) % i == 0
            ):
                track.append(i)
                backtrack(track)
                track.pop()

    backtrack()
    return res
