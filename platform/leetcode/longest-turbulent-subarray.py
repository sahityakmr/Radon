from functools import lru_cache
from typing import List


class LongestTurbulentSubarray:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        @lru_cache(None)
        def dp(i, dr):
            if i == 0 or (arr[i] - arr[i - 1]) * dr >= 0: return 1
            return dp(i - 1, -dr) + 1

        return max(dp(i, dr) for i in range(len(arr)) for dr in [-1, 1])


res = LongestTurbulentSubarray().maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9])
print(res)
