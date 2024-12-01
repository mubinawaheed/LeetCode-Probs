from typing import List

# Given an array arr of integers, check if there exist two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        for i in range(len(arr)):
            if(2*arr[i] in arr and arr.index(2*arr[i]) != i):
                return True
        return False
        
        
        
