from collections import defaultdict
from typing import Counter, List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        res=0
        n=len(nums)
        s=defaultdict(int)
        equalPairs=0
        r=0
        for i in range(len(nums)):
            while (r < n and equalPairs<k):
                s[nums[r]]+=1
                if s[nums[r]] >=2:
                    equalPairs+=(s[nums[r]]-1)
                r+=1
            if equalPairs>=k:
                res += (n-r+1)

            s[nums[i]]-=1
            if s[nums[i]]>=1:
                 equalPairs-=s[nums[i]]
        return res

s=Solution()
a=s.countGood( [3,1,4,3,2,2,4], 2)
print(a)