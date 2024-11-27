#  Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space. 

class Solution(object):
    
    #Un optimized solution
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in range(len(nums)):
            
            if (d.get(nums[i]) is not None):
                
                d[nums[i]]+=1
            else:
                
                d[nums[i]]=1
                
        d = next(((k, v) for k, v in d.items() if v == 1), None)

        return d[0]

    def singleNumberOptimized(self, nums): # using bitwise exclusive XOR. 2 XOR 2 = 0 but 2 XOR 0 =2
        res=0
        for i in nums:
            res = i ^ res
        return res
    
