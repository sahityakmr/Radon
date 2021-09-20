from typing import List


def jas(nums1, nums2):
    var = set(nums1) and set(nums2)
    print(var)
    pass


class ListIntersection:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        dict2 = {}

        for num in nums1:
            if num in dict1.keys():
                dict1[num] = dict1[num] + 1
            else:
                dict1[num] = 1

        for num in nums2:
            if num in dict2.keys():
                dict2[num] = dict2[num] + 1
            else:
                dict2[num] = 1

        res = []
        for key in dict1.keys():
            if key in dict2.keys():
                freq = min(dict1[key], dict2[key])
                for i in range(freq):
                    res.append(key)
        return res


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
nums3 = [2, 2, 2, 1]
nums4 = [2, 2, 2, 2, 2, 2, 2, 1, 1, 3, 4, 5, 6, 7]
# ListIntersection().intersect(nums1, nums2)
res = ListIntersection().intersect(nums3, nums4)
print(res)
