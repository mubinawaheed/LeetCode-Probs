class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            a=s.find(part)
            s=s[0:a] + s[a+len(part):]    
        return s
    
s=Solution()
print(s.removeOccurrences("gjzgbpggjzgbpgsvpwdk", "gjzgbpg"))