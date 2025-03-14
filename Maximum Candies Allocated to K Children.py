from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        s=sum(candies)
        if s<k:
            return 0
        l=1
        r=s//k
        res=0
        while l<=r:
            mid = (l+r)//2
            count=0
            for c in candies:
                if c>=mid:
                    count+=(c//mid)
                if count>=k:
                    break
            if count>=k:
                res = mid
                l=mid+1
            else:
                r=mid-1
        return res