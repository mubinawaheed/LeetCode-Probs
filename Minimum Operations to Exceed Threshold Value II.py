import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        m=None
        heapq.heapify(nums)
        ops=0
        while len(nums)>=2:
            if (nums[0] >= k):
                break
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums,(min(x, y) * 2 + max(x, y)))
            ops+=1

        return ops
    
s=Solution()
p=s.minOperations([2,11,10,1,3],10)