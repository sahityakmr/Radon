class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        temp = res = (left & right)
        if res * 2 < right:
            return 0
        if left == right:
            return res
        mask = (1 << 32) - 1
        mask1 = res ^ left
        mask1 = mask1 ^ mask
        mask2 = res ^ right
        mask2 = mask2 ^ mask
        mask3 = mask1 & mask2

        mask = (1 << 32) - 1
        mask = mask << 1
        mask2 = 1
        while mask & mask3 > 0:
            if mask2 & mask3 == 0:
                mask3 = mask3 & mask
            mask2 = mask2 << 1
            mask = mask << 1
        return res & mask3


print(Solution().rangeBitwiseAnd(5, 7))
