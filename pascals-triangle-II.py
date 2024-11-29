
import math
from typing import List
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# Input: rowIndex = 3
# Output: [1,3,3,1]

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lst=[]
        for i in range(rowIndex+1):
            lst.append(math.factorial(rowIndex) // (math.factorial(i) * math.factorial(rowIndex - i)))

        return lst