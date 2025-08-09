class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:  # Base case: negative or zero is not a power of two
            return False
        if n == 1:  # Base case: 2^0 = 1
            return True
        if n % 2 != 0:  # If n is not divisible by 2, it’s not a power of two
            return False
        return self.isPowerOfTwo(n // 2)
        
from cmath import log


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1 or n==2:
            return True
        if n%2 != 0 or n<=0:
            return False

        x = log(abs(n)) / log(2)

        if abs(x - round(x)) < 1e-9:
            return True
        return False