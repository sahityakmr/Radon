import collections
from typing import List


class Solution:

    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        r, c = len(matrix), len(matrix[0])
        rank = [0] * (r + c)
        d = collections.defaultdict(list)
        for i in range(r):
            for j in range(c):
                d[matrix[i][j]].append([i, j])

        def find(k):
            if p[k] != k:
                return find(p[k])
            return k

        for key in sorted(d):
            rank2 = rank[:]
            p = [i for i in range(r + c)]
            for i, j in d[key]:
                i, j = find(i), find(r + j)
                p[i] = j
                rank2[j] = max(rank2[i], rank2[j])
            for i, j in d[key]:
                rank[i] = rank[r + j] = matrix[i][j] = rank2[find(i)] + 1
        return matrix


print(Solution().matrixRankTransform([[20, -21, 14], [-19, 4, 19], [22, -47, 24], [-19, 4, 19]]))
print(Solution().matrixRankTransform([[20, -21, -20], [-19, 4, 19], [22, -47, 24], [-19, 4, -20]]))
