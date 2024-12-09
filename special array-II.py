from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
    
        my_list = [1] * len(nums)
        print(my_list)
        for i in range(1,len(nums)):
            prev = nums[i-1]%2 == 0
            nextE = nums[i]%2 == 0
            if(prev!=nextE):
                my_list[i] = my_list[i-1]+my_list[i]

        ans=[]
        for k in range(len(queries)):
            if(queries[k][1]-queries[k][0]+1 > my_list[queries[k][1]]):
                ans.append(False)
            else:
                ans.append(True)
        return ans
            
            