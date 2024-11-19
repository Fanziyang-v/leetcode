"""
Subset I.

Link: https://leetcode.cn/problems/subsets/
"""


def combinations(nums: list[int], n: int) -> list[list[int]]:
    res: list[list[int]] = []

    def backtrack(choices: list[int], track: list[int] = []) -> None:
        nonlocal res
        if len(track) == n:
            res.append(track[:])
            return
        for i in range(len(choices)):
            track.append(choices[i])
            backtrack(choices[i + 1 :])
            track.pop()

    backtrack()
    return res


def subsets(nums: list[int]) -> list[list[int]]:
    res: list[list[int]] = []
    for n in range(len(nums) + 1):
        res += combinations(nums, n)
    return res
