class Solution:
    def clearDigits(self, s: str) -> str:
        l=[]
        for i in range(len(s)):
            if s[i].isdigit():
                l.pop()
            else:
                l.append(s[i])


        return ''.join(l)
k=Solution()
k.clearDigits('cb34')