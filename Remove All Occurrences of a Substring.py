class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            a=s.find(part)
            s=s[0:a] + s[a+len(part):]    
        return s

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack=[]
        
        for i in s:
            stack.append(i)
            if (len(stack)>=len(part) and ''.join(stack[-len(part):])==part):
                for j in range(len(part)):
                    stack.pop()
        return "".join(stack)
                    
    
s=Solution()
print(s.removeOccurrences("daabcbaabcbc", "abc"))