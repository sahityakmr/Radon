class Solution:
    def fib(self, n: int) -> int:
        a = -1
        b = 1
        c = 0
        for i in range(n + 1):
            c = a + b
            a = b
            b = c
        return c


print(Solution().fib(1))
print(Solution().fib(2))
print(Solution().fib(3))