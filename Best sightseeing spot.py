from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        firstP= values[0]+0
        maxPairSum = 0
        for i in range(1,len(values)):
            a=values[i]-i
            maxPairSum = max(maxPairSum, a+firstP)
            firstP = max(firstP, values[i]+i)

        return maxPairSum
    
    
s=Solution()
print(s.maxScoreSightseeingPair([8,1,5,2,6,21,25,7]))