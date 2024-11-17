"""
Letter Combinations of a Phone Number.

Link: https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
"""

digit2letters: dict[str, list[str]] = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


def letter_combinations(digits: str) -> list[str]:
    if not digits:
        return []
    res: list[str] = []

    def backtrack(digits: str, track: list[str] = []) -> None:
        nonlocal res
        if not digits:
            res.append("".join(track))
            return
        for letter in digit2letters[digits[0]]:
            track.append(letter)
            backtrack(digits[1:], track)
            track.pop()

    backtrack(digits)
    return res
