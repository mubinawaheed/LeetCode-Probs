class Solution:
    def smallestNumber(self, n: int) -> int:
        a=bin(n).replace('0b', '')
        return 2**len(a) - 1
        