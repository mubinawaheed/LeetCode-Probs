from typing import Counter, List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort(reverse=True)
        s=Counter(arr)
        for k, v in s.items():
            if k == v:
                return k
        return -1