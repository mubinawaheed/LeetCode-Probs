class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res=0

        curr=0
        even=0
        odd=0
        for i in range(len(arr)):
            curr+=arr[i]
            if curr%2 != 0 :
                res+=1+even
                odd+=1
                
            else:
                res+=odd
                even+=1
            
        return res %  (10**9 + 7)

