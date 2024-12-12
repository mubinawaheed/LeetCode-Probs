from typing import List
from math import floor, sqrt

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            maxV = max(gifts)
            index = gifts.index(maxV) 
            gifts[index] = floor(sqrt(maxV))
        return sum(gifts)