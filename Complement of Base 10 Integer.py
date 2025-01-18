class Solution:
    def bitwiseComplement(self, n: int) -> int:
        a=len(bin(n).replace("0b", ''))
        b=a*'1'
        return abs(n-int(b,2))