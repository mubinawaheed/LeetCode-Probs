# Given a positive integer n, find the pivot integer x such that:

# The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
# Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

#Prefix sum problem

class Solution:
    def pivotInteger(self, n: int) -> int:
        
        #smart solution
        sumN= int((n+1)*(n/2))
        pivot=int(sumN**0.5)
        if pivot*pivot == sumN:
            return pivot
        return -1
        
        #BruteForce
        l=list(range(1,n+1))

        for j, val in enumerate(l):
            if sum(l[0:j+1]) == sum(l[j: ]):
                return val
        return -1

        