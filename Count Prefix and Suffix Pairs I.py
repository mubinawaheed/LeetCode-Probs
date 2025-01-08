from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        count=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if (self.isPrefixAndSuffix(words[i], words[j])):
                    count+=1
        return count

    
    def isPrefixAndSuffix(self, s1, s2):
        if len(s1)>len(s2):
            return False
        return s2[0:len(s1)] == s1 and s2[len(s2)-len(s1):] ==s1
        