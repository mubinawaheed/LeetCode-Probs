class Solution(object):
    def checkPowersOfThree(self, n):
        
        while n > 0:
            if n % 3 == 2:  # If any ternary digit is 2, we can't form `n` using distinct powers of 3
                return False
            n //= 3  # Reduce n by dividing by 3
        return True
    
s=Solution()
s.checkPowersOfThree(21)