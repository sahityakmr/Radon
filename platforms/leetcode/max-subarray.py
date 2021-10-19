from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_yet = -99999
        sum = 0
        max_sum = 0
        for i in range(len(nums)):
            max_yet = max(max_yet, nums[i])
            sum += nums[i]
            max_sum = max(max_sum, sum)
            if sum < 0:
                sum = 0
        if max_yet < 0:
            return max_yet
        return max_sum


