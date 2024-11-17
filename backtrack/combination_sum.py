"""
Combination Sum.

Link: https://leetcode.cn/problems/combination-sum/
"""


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    res: list[list[int]] = []

    def backtrack(target_sum: int, track: list[int] = []) -> None:
        nonlocal res
        if target_sum == 0:
            res.append(track[:])
            return
        for num in candidates:
            if target_sum >= num and (not track or num >= track[-1]):
                track.append(num)
                backtrack(target_sum - num, track)
                track.pop()

    backtrack(target)
    return res
