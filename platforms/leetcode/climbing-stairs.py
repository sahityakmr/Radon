def fib(n):
    a = 0
    b = 1
    c = 0
    for i in range(n):
        c = a + b
        a = b
        b = c
    return c


class Solution:
    def climbStairs(self, n: int) -> int:
        return fib(n)

print(Solution().climbStairs(2))