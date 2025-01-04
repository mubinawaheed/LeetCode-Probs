class Solution:
    @staticmethod
    def lengthOfLongestSubstring( s: str) -> int:
       
        start=0
        count=0
        res=set()
        ans=[]
        for i in range(len(s)):
            if s[i] not in res:
                res.add(s[i])
                count=max(count, len(res))
            else:
                ans.append(count)
                while s[i] in res:
                    res.remove(s[start])
                    start+=1
                res.add(s[i])
        ans.append(count)
        return max(ans)

ans=Solution.lengthOfLongestSubstring('pwwkew')
print(ans)