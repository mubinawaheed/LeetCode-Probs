from typing import List
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s={}
        for i in range(len(nums)):
            if nums[i] in s:
                if (abs(s[nums[i]][0]-i) <= k):
                    return True
                else:
                    s[nums[i]][1]+=1
                    s[nums[i]][0] = i
            else:
                s[nums[i]] = [i, 1]
        return False
                