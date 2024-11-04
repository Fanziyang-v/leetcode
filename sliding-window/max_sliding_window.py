"""
Sliding Window Maximum.

Link: https://leetcode.cn/problems/sliding-window-maximum/
"""


class MonotonicQueue:
    def __init__(self) -> None:
        self.data = []

    def push(self, value: int) -> None:
        while self.data and self.data[-1] < value:
            self.data.pop()
        self.data.append(value)

    def pop(self) -> int:
        self.data.pop(0)

    def peek(self) -> int:
        return self.data[0]


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    res: list[int] = []
    monotonic_queue = MonotonicQueue()
    for i in range(len(nums)):
        monotonic_queue.push(nums[i])
        if i + 1 >= k:
            res.append(monotonic_queue.peek())
            if monotonic_queue.peek() == nums[i - k + 1]:
                monotonic_queue.pop()

    return res
