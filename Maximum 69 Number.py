class Solution:
    def maximum69Number (self, num: int) -> int:
        s=str(num)
        res=[]
        f=False
        for n in range(len(s)):
            if s[n]=='6' and not f:
                res.append('9')
                f=True
            elif f or s[n]=='9':
                res.append(s[n])
            
        return int(''.join(res))
