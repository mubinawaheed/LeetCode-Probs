class Solution:
    def reverse(self, x: int) -> int:
        sign=1
        sign *= -1 if x<0 else 1
        x=abs(x)

        num = 0
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        while x>0:
            num  = (num*10) + (x%10)
            
            if num * sign > INT_MAX or num * sign < INT_MIN:
                return 0
            x=x//10

        return num*sign
        
        
s=Solution()
p=s.reverse(-123)