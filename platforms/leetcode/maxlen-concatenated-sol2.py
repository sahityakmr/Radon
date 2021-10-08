from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def max_len_of_merged_word(words):
            largest, M = 0, len(words)
            for i in range(M):
                alpha1 = set(words[i])
                size = len(words[i])
                for j in range(M):
                    if j == i: continue
                    alpha2 = set(words[j])
                    if alpha1.isdisjoint(alpha2):
                        size += len(words[j])
                        alpha1 = alpha1.union(alpha2)
                if largest < size: largest = size
            return largest

        # select unique words
        N = len(arr)
        unique = [False] * N
        for i in range(N):
            alpha = set(arr[i])
            if len(arr[i]) == len(alpha): unique[i] = True

        # sort(bucket) arr[i] by its length
        tmp = []
        for i in range(27): tmp.append([])
        for i in range(N):
            if unique[i]:
                tmp[len(arr[i])].append(arr[i])
        strs = []
        for i in range(1, 27): strs += tmp[i]

        # get maximum length of merged word
        largest = max_len_of_merged_word(strs)
        strs.reverse()
        largest = max(largest, max_len_of_merged_word(strs))

        return largest
