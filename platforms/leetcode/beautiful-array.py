from itertools import permutations


class BeautifulArray:
    def beautifulArray(self, n: int):
        # return self.naive(n)
        # return self.recursive([i for i in range(1, 1 + n)])
        return self.one_liner(n)

    def naive(self, n):
        for perm in permutations(range(1, n + 1)):
            if not self.invalid(perm):
                return perm
        pass

    def invalid(self, x):
        n = len(x)
        flag = False
        for i in range(n):
            if flag:
                break
            for j in range(i + 2, n):
                if flag: break
                for k in range(i + 1, j):
                    if 2 * x[k] == x[i] + x[j]:
                        flag = True
                        break
        return flag

    def recursive(self, nums):
        if len(nums) <= 2:
            return nums
        return self.recursive(nums[::2]) + self.recursive(nums[1::2])

    def one_liner(self, n):
        return sorted(range(1, n + 1), key=lambda x: bin(x)[:1:-1])
