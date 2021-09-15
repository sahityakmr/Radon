from typing import List


class MostStoneRemoved:
    def removeStone(self, stone: List[List[int]]) -> int:
        uf = {}

        def find(x):
            if x != uf.setdefault(x, x):
                uf[x] = find(uf[x])
            return uf[x]

        for i, j in stone:
            uf[find(i)] = find(-j)
        return len(stone) - len({find(x) for x in uf})
