class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            v = s[i+1:]+s[0:i+1]
            if v==goal:
                return True
        return False
        