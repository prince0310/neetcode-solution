
from collections import defaultdict
from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.timeMap[key]

        # Binary search for the first timestamp greater than
        # the requested timestamp
        left = 0
        right = len(values)

        while left < right:
            mid = (left + right) // 2

            if values[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid

        # left is now the position just after the best timestamp
        if left == 0:
            return ""

        return values[left - 1][1]
