class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        while True:
            while  i<len(nums)-1 and nums[i]==nums[i+1]:
                del nums[i]
            i+=1
            if(i>=len(nums)-1):
                break
                
            