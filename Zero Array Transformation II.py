from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        k=0
        diff_arr = [0]*(len(nums)+1)
        sm=0
        #  the goal is to increment the values at diff_arr[i] until it matches nums[i]
        for i in range(len(nums)):
            while sm + diff_arr[i] < nums[i]: # continously update the element until it becomes 0
                if k == len(queries):
                    return -1
                l,r,v = queries[k]
                k+=1
                if r<i:
                    continue # useless query already updated the element in past
                diff_arr[max(l,i)]+=v
                diff_arr[r+1]-=v
            sm+=diff_arr[i]
        return k



        # i=0
        # while sum(nums)>0 and i<len(queries):
        #     l,r,v=queries[i]
        #     for j in range(l,r+1):
        #         if nums[j]>=v:
        #             nums[j]-=v
        #         else:
        #             nums[j] =0
        #     i+=1
        # if sum(nums)==0:
        #     return i
        # else:
        #     return -1
