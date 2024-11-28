from typing import List
# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[]
        for i in range(numRows):
            arr=[1]
            if i == 0:
                result.append(arr)
            else:
                for j in range(1, i): 
                    element = result[i-1][j-1] + result[i-1][j]
                    arr.append(element)
                arr.append(1)
                result.append(arr)
        return result