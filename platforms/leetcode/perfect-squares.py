import math
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def numSquares(self, n: int) -> int:
        start = int(math.floor(math.sqrt(n)))
        if start * start == n:
            return 1
        min_val = 9999
        for val in range(start, 0, -1):
            res = self.numSquares(n - val * val)
            min_val = min(min_val, res)
        return 1 + min_val


print(Solution().numSquares(8441))
