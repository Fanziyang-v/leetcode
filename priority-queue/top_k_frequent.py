"""
Top K Frequent Words.

Link: https://leetcode.cn/problems/top-k-frequent-words/
"""
from heapq import heapify, heappop

def top_k_frequent(words: list[str], k: int) -> list[str]:
    res: list[str] = []
    word2num: dict[str, int] = {}
    for word in words:
        word2num[word] = word2num.get(word, 0) + 1
    min_heap = [(-num, word) for word, num in word2num.items()]
    heapify(min_heap)
    for _ in range(k):
        _, word = heappop(min_heap)
        res.append(word)
    return res
