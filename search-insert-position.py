# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # using binary search algorithm for searching
        low=0
        high=len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if(nums[mid]==target):
                return mid
            elif(target>nums[mid]):
                low = mid+1
            elif(target<nums[mid]):
                high = mid-1
                
        if (target>nums[-1]):
            nums.append(target)
            return len(nums)-1
        elif(target<nums[0]):
            nums.insert(0, target)
            return 0
        else:
            for i in range(0, len(nums)-1):
                if(target>nums[i] and target<nums[i+1]):
                    nums.insert(i+1, target)
                    return i+1
            
        
        


        