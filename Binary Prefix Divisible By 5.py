from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res=[]
        s=''
        for i in range(len(nums)):
            s+=str(nums[i])

        for j in range(len(s)):
            res.append(int(s[0:j+1],2) % 5 == 0)
        return res



s=Solution()
a=s.prefixesDivBy5([0,1,1,1,1,1])