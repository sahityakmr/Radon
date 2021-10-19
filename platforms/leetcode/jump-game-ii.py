from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curr_farthest = 0
        curr_max = 0
        for i in range(len(nums) - 1):
            curr_farthest = max(curr_farthest, i + nums[i])
            if i == curr_max:
                jumps += 1
                curr_max = curr_farthest
        return jumps

