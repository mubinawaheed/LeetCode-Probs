class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if (len(a) != len(b)):
            d=abs(len(a) - len(b))
            if len(a)>len(b):
                i='0'*d
                i+=b
                b=i
            else:
                i='0'*d
                i+=a
                a=i
        c=0
        print(a,b)
        res=''
        for i in range(len(a)-1,-1,-1):
            a1=int(a[i],2)
            b2=int(b[i],2)
            total = a1+b2+c
            res = str(total%2) + res
            c=total//2
        if c:
            res=str(c)+res
        return res





        