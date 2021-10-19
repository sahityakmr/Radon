import math
from functools import lru_cache


class Solution:
    def __init__(self):
        self.min_count = None

    def numSquares(self, n: int) -> int:
        self.min_count = [99999] * (n + 1)
        self.min_count[0] = 0
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                self.min_count[i] = min(self.min_count[i], self.min_count[i - j * j] + 1)
                j += 1
        return self.min_count[-1]


print(Solution().numSquares(8441))
