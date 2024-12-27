from typing import List

# - MEDIUM
# You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

# The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

# Return the maximum score of a pair of sightseeing spots.
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