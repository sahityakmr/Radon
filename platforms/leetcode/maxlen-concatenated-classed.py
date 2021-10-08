from typing import List

dic = {}


def ston(s):
    num = 0
    for c in s:
        offset = (1 << (ord(c) - ord('a')))
        if (num & offset) == 0:
            num = (num | offset)
        else:
            return -1
    return num


def setbits(num):
    setb = 0
    while num > 0:
        setb += (num & 1)
        num = num >> 1
    return setb


def findMax(num, nstr, ind):
    if ind in dic and num in dic[ind]:
        return dic[ind][num]
    if ind >= len(nstr):
        if ind not in dic:
            dic[ind] = {}
        dic[ind][num] = setbits(num)
        return dic[ind][num]
    if (num & nstr[ind]) > 0:
        if ind not in dic:
            dic[ind] = {}
        dic[ind][num] = findMax(num, nstr, ind + 1)
        return dic[ind][num]
    if ind not in dic:
        dic[ind] = {}
    dic[ind][num] = max(findMax((num | nstr[ind]), nstr, ind + 1), findMax(num, nstr, ind + 1))
    return dic[ind][num]


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        global dic
        dic = {}
        nstr = []
        for s in arr:
            k = ston(s)
            if k > 0:
                nstr.append(k)
        return findMax(0, nstr, 0)


print(Solution().maxLength(["un", "iq", "ue"]))
print(Solution().maxLength(["cha", "r", "act", "ers"]))
print(Solution().maxLength(["yy","bkhwmpbiisbldzknpm"]))
