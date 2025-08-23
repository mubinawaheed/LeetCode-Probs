class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        v=set()
        res=0
        start=0
        end = len(s) -1
        for i in range(len(s)):
            while s[i] in v:
                v.remove(s[start])
                start +=1
            v.add(s[i])
            
            res = max(res, i-start+1)


        return res 