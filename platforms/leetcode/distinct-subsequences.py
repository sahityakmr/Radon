class DistinctSubsequences:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for i in range(len(s) + 1)] for j in range(len(t) + 1)]
        for i in range(len(s) + 1):
            dp[0][i] = 1
        for i in range(len(t)):
            for j in range(len(s)):
                if t[i] == s[j]:
                    dp[i + 1][j + 1] = dp[i][j] + dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]
        return dp[len(t)][len(s)]

res = DistinctSubsequences().numDistinct("babgbag", "bag")
print(res)