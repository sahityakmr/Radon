import collections
import queue
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = collections.defaultdict(lambda: 0)
        stack = queue.LifoQueue()
        for i in range(len(nums2) - 1, -1, -1):
            next_higher = -1
            while not stack.empty():
                top = stack.get()
                if top > nums2[i]:
                    next_higher = top
                    stack.put(top)
                    break
            dict[nums2[i]] = next_higher
            stack.put(nums2[i])

        res = [0] * len(nums1)
        for i in range(len(nums1)):
            res[i] = dict[nums1[i]]
        return res


print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
print(Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]))
