from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if(len(nums)<1):
            return []
        r=[nums[0]]
        res=[]
        for i in range(1,len(nums)):

            if abs(r[-1] - nums[i]) == 1:
                r.append(nums[i])
            else:
                if len(r)>1:
                    res.append(str(r[0]) + "->" + str(r[-1]))
                elif len(r)==1:
                    res.append(str(r[0]))
                r= [nums[i]]
        if len(r)>1:
            res.append(str(r[0]) + "->" + str(r[-1]))
        elif len(r)==1:
            res.append(str(r[0]))
        return res

            
            