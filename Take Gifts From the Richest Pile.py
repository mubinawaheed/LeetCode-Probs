from typing import List
from math import floor, sqrt

import heapq
#finding the max value is O(n). and doing it k times can lead to O(n*k) time complexity. so we'll use heap.
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            maxV = max(gifts) # takes O(n) time. We can use a heap to do this in O(log n) time.
            index = gifts.index(maxV) 
            gifts[index] = floor(sqrt(maxV))
        return sum(gifts)
    
    #Using heap. List -> Heap takes O(n) time
    def pickGiftsOptimized(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)
        for i in range(k):
            n = -heapq.heappop(gifts)
            heapq.heappush(gifts, -floor(sqrt(n)))
            
        return -sum(gifts)
            