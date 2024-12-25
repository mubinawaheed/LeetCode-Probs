from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2)) #set intersection - 4ms
 
        #brute force - 10ms
        if(len(nums1) < len(nums2)):
            s = {num for num in nums1 if num in nums2}
            return list(s)

        else:
            s = {num for num in nums2 if num in nums1}
            return list(s)

        
        