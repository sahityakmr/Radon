from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dupes = []
        for i in range(len(nums)):
            k = nums[i]
            if k < 0:
                k *= -1
            if nums[k - 1] < 0:
                dupes.append(k)
            else:
                nums[k - 1] *= -1
        return dupes


print(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
