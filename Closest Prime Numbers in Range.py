from cmath import sqrt
from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Sieve of Eratosthenes 
        prime=[True]*(right+1)
        prime[0]=prime[1]=False
        for i in range(2, int(sqrt(right))+1):
            if (not prime[i]):
                continue
            for j in range(i+i, right+1, i):
                prime[j]=False
        nums=[]
        for k in range(left, right+1):
            if (prime[k]):
                nums.append(k)

        if (len(nums)<2):
            return [-1, -1]
        res=[]
        diff= float('inf')
        for i in range(len(nums)-1):
            if ((nums[i+1] - nums[i])< diff):
                diff=nums[i+1] - nums[i]
                res=[nums[i], nums[i+1]]
            if (diff == 2):
                break
        return res

