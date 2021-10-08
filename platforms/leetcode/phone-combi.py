from typing import List

numMap = {
    "2": ['a', 'b', 'c'],
    "3": ['d', 'e', 'f'],
    "4": ['g', 'h', 'i'],
    "5": ['j', 'k', 'l'],
    "6": ['m', 'n', 'o'],
    "7": ['p', 'q', 'r', 's'],
    "8": ['t', 'u', 'v'],
    "9": ['w', 'x', 'y', 'z'],
}


def findAll(name, digits, ind, res):
    if ind == len(digits):
        res.append("".join(name))
        return
    for char in numMap[digits[ind]]:
        name.append(char)
        findAll(name, digits, ind + 1, res)
        name.pop()


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits) == 0:
            return res
        findAll([], digits, 0, res)
        return res


print(Solution().letterCombinations("23"))
