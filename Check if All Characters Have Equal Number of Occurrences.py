
# Given a string s, return true if s is a good string, or false otherwise.

# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
 
        sp={}
        for i in s:
            if i in sp:
                sp[i] +=1
            else:
                sp[i]=1
        return len(set(sp.values())) == 1
