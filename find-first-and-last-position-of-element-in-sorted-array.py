from typing import List
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

#LEETCODE MEDIUM
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a=self.binSearch(nums, True, target)
        b= self.binSearch(nums, False, target)
        return [a,b]

    def binSearch(self,nums, bias, target):
        start=0
        end=len(nums)-1
        i=-1
        while start<=end:
            mid =(start+end)//2
            if (nums[mid]==target):
                i=mid
                if(bias):
                    end = mid-1
                else:
                    start = mid+1
            elif(nums[mid]<target):
                start = mid+1
            else:
                end = mid-1
        return i