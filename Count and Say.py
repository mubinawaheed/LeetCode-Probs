class Solution:
    def countAndSay(self, n: int) -> str:
        

        def rle(s, i):
            if i>=n:
                return s
            newStr = ""
            count = 1
            for j in range(1, len(s)):
                if s[j] == s[j-1]:
                    count += 1
                else:
                    newStr += str(count) + s[j-1]
                    count = 1
            newStr += str(count) + s[-1]


            return rle(newStr, i+1)

        return rle('1', 1)
       