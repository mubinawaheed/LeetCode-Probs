from collections import defaultdict
from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res=[]
        s=defaultdict(int)
        for i in range(len(nums1)):    
            s[nums1[i][0]] = nums1[i][1]

        for i in range(len(nums2)):
            s[nums2[i][0]] = s[nums2[i][0]] + nums2[i][1]

        for key, val in sorted(s.items()):
            res.append([key, val])
        return res