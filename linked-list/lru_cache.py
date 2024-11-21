"""
LRU Cache.

Link: https://leetcode.cn/problems/lru-cache/
"""


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: dict[int, int] = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self._make_recently(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                # Remove the least recently used item becuase cache is full.
                self.cache.pop(next(iter(self.cache)))
            self.cache[key] = value
        else:
            del self.cache[key]
            self.cache[key] = value

    def _make_recently(self, key: int) -> None:
        val = self.cache[key]
        del self.cache[key]
        self.cache[key] = val
