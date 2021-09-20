from functools import lru_cache

dict = [[-1 for i in range(46)] for j in range(46)]


def climb(curr, target):
    if dict[curr][target] != -1:
        return dict[curr][target]
    if curr == target:
        return 1
    if curr > target:
        return 0
    ans = climb(curr + 1, target) + climb(curr + 2, target)
    dict[curr][target] = ans
    return ans


class StepClimb:
    def climbStairs(self, n: int) -> int:
        return climb(0, n)
