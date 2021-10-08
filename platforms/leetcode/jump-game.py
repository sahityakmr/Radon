from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        i = 0
        while i < min(maxReach + 1, len(nums)):
            maxReach = max(maxReach, i + nums[i])
            if maxReach >= len(nums) - 1:
                return True
            i += 1
        return False


print(Solution().canJump([2, 3, 1, 1, 4]))
