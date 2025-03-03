from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]: # space optimized
        res=[0]*len(nums)
        i,j = 0 ,( len(nums)-1)
        i2, j2 = 0,(len(nums)-1)
        
        while i <len(nums):
            if nums[i] < pivot:
                res[i2]=nums[i]
                i2+=1
            if nums[j]>pivot:
                res[j2] = nums[j]
                j2-=1

            i+=1
            j-=1

        while i2<=j2:
          
            res[i2]= res[j2]=pivot
            i2+=1
            j2-=1
        return res
    
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        r1=[]
        r2=[]
        q=[]
        for n in nums:
            if n>pivot:
                r2.append(n)
            elif n<pivot:
                r1.append(n)
            else:
                q.append(n)
        return r1+q+r2
        
