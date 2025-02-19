class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        choices='abc'
        res=[]
        total = 3*(2**(n-1))
        low=1
        high = total
        for i in range(n):
            curr = low
            partition = (high-low+1)//len(choices)

            for c in choices:
                if k in range(curr, curr+partition):
                    res.append(c)
                    low = curr
                    high = curr+partition-1
                    choices = 'abc'.replace(c,'')
                    break
                curr+=partition

        return ''.join(res)
    
class Solution:

    def getHappyString(self, n: int, k: int) -> str:
        happystrings=[]
        currentStr=''
        self.generate_strings(n, k, currentStr, happystrings)

        if len(happystrings)<k:
            return ''

        return happystrings[k-1]   

    def generate_strings(self,n,k, currStr, happystrings):
        if len(currStr) == n:
            happystrings.append(currStr)
            return

        for c in ['a', 'b', 'c']:
            if len(currStr) >0 and currStr[-1] == c:
                continue
            self.generate_strings(n,k,currStr+c, happystrings)
            if len(happystrings) == k:
                return

s=Solution()
s.getHappyString(3,4)