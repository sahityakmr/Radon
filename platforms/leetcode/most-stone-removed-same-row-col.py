from typing import List


class MostStoneRemoved:
    def removeStones(self, stone: List[List[int]]) -> int:
        uf = {}

        def find(x):
            if x != uf.setdefault(x, x):
                uf[x] = find(uf[x])
            return uf[x]

        for i, j in stone:
            uf[find(i)] = find(~j)
        return len(stone) - len({find(x) for x in uf})


#res = MostStoneRemoved().removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]])
res = MostStoneRemoved().removeStones([[0,1],[1,0]])
print(res)
