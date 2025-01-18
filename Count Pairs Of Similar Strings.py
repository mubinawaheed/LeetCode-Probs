from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        u=0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if (set(words[i]) == set(words[j])):
                    u+=1
        return u
        