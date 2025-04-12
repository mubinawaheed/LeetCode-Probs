class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res=0
        for n in range(low, high+1):
            a=str(n)
            if len(a) % 2 != 0:
                continue
            if sum(map(int, a[:len(a)//2])) == sum(map(int, a[len(a)//2:])):
                res+=1
        return res
        