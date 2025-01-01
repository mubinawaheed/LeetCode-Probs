# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
from collections import Counter

class Solution:
    def maxScore(self, s: str) -> int:
        som=0
        
        for i in range(len(s)-1):
            a=s[0:i+1]
            b=s[len(a): ]
            counterA= Counter(a)
            counterB = Counter(b)
            som=max(som, counterA['0']+counterB['1'])
        return som
            

s=Solution()
print(s.maxScore("1111"))