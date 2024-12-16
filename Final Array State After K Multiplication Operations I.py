# class Solution:
import heapq
from typing import List


def getFinalState( nums: List[int], k: int, multiplier: int) -> List[int]:
    pq=[]
    for i in range(len(nums)):
        heapq.heappush(pq, ( nums[i], i))
        
    for _ in range(k):
        v, index=heapq.heappop(pq)
        nums[index] = v*multiplier
        heapq.heappush(pq, ( v*multiplier, index))
    return nums

a=getFinalState([1,2], 3,4)