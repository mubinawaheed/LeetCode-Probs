from typing import Counter, List


class Solution:
    def sortColors(self, nums: List[int]) -> None: # can also be sort using quick sort

        s=Counter(nums)
        for i in range(len(nums)):
            if s[0]>=0:
                nums[i]=0
                s[0]-=1
            if s[1]>=0 and s[0]<0:
                nums[i]=1
                s[1]-=1
            if s[2]>=0 and s[1]<0 and s[0]<0:
                nums[i]=2
                s[2]-=1
    #     def quickSort(array, left, right ):
    #         if left < right:
    #             pivot = self.partition(array, left, right)
    #             quickSort(array, left, pivot-1)
    #             quickSort(array, pivot+1, right)
        
    #     quickSort(nums,0, len(nums)-1)

    # def partition(self,array, left, right):

    #     i = left
    #     j = right-1
    #     pivot = array[right]
    #     while i<j:
    #         while  i<right and array[i]<pivot :
    #             i += 1
    #         while array[j]>=pivot and j>left:
    #             j-=1
    #         if i < j:
    #             array[i], array[j] = array[j], array[i]
            
    #     if(array[i]>pivot):
    #         array[i], array[right] = array[right], array[i]
            
    #     return i
