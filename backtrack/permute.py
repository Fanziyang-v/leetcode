"""
Permutations.

Link: https://leetcode.cn/problems/permutations/
"""


def permute(nums: list[int]) -> list[list[int]]:
    res: list[list[int]] = []
    n = len(nums)

    def backtrack(track: list[int] = []) -> None:
        nonlocal res
        if len(track) == n:
            res.append(track[:])
            return
        for num in nums:
            if num not in track:
                track.append(num)
                backtrack(track)
                track.pop()

    backtrack()
    return res
