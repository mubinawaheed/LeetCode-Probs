import heapq
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        h=[]
        for i in range(len(nums)):
            h.append((nums[i], i))
        heapq.heapify(h)
        indexes = set()
        for i in range(len(h)):
            n = heapq.heappop(h)
            if(n[1] not in indexes):
                score += n[0]
                indexes.add(n[1])
                indexes.add(n[1]+1)
                indexes.add(n[1]-1)
            print(n)
            
        return score

a = findScore([10,44,10,8,48,30,17,38,41,27,16,33,45,45,34,30,22,3,42,42])

print(a)