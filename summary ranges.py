from typing import List
# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b

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

            
            