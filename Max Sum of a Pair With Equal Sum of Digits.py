from collections import defaultdict
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        pairs=defaultdict(int)
        max_sum=-1
        
        for i in range(len(nums)):  # More Optimized
            k=self.getSum(nums[i])
            if (pairs[k] < 1):
                pairs[k] = nums[i]

            else:
              
                max_sum = max(max_sum, nums[i]+pairs[k])
                if (nums[i] > pairs[k]):
                    pairs[k] = nums[i]

        # for j in pairs.values():  #Also okayy - but above os more optimized
        #     if len(j) <2:
        #         continue
        #     a = max(j)
        #     j.remove(a)
        #     b = max(j)
          
        #     max_sum=max(max_sum , a+b)
        return max_sum



    def getSum(self,k):
        w=0
        while k>0:
            w+=(k%10)
            k=k//10
        return w
        