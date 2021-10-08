from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        eIndex = 0
        oIndex = 1

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                tmp = nums[i]
                nums[i] = nums[eIndex]
                nums[eIndex] = tmp
                eIndex += 2
            else:
                tmp = nums[i]
                nums[i] = nums[oIndex]
                nums[oIndex] = tmp
                oIndex += 2
        return nums


print(Solution().sortArrayByParityII([4, 2, 5, 7]))
