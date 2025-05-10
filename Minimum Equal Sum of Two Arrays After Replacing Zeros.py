from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        count1=0
        count2=0

        for i in range(len(nums1)):
            if nums1[i]==0:
                count1+=1
                nums1[i]+=1
        for i in range(len(nums2)):
            if nums2[i]==0:
                count2+=1
                nums2[i]+=1
        a=sum(nums1)
        b=sum(nums2)
        if (a>b and count2==0):
            return -1
        if (a<b and count1==0):
            return -1

        return max(a,b)