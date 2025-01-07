# Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

# A substring is a contiguous sequence of characters within a string
from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if (i!=j and words[i] in words[j]):
                    res.append(words[i])
                    break
        return res
    