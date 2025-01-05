class Solution:
    def isPalindrome(self, x: int) -> bool:
        # intuition break the number if both halfs are similar then number is a palindrom
        #e.g. 1221 -> 12 and 12 yes

        if x<0 or( x!=0  and x%10 == 0):
            return False

        half = 0

        while half<x:
            half = (x%10) + (half*10)
            x=x//10

        return half==x or x==half//10