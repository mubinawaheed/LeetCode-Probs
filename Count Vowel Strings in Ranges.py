from typing import List

# You are given a 0-indexed array of strings words and a 2D array of integers queries.

# Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

# Return an array ans of size queries.length, where ans[i] is the answer to the ith query.
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans=[]
        vowels = set([ 'a', 'e', 'i', 'o', 'u'])
        count=[0]*(len(words)+1)
        prev=0
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prev+=1    
            count[i+1]=prev

        for i in range(len(queries)):
            answer = count[queries[i][-1]+1]- count[queries[i][0]]
            ans.append(answer)     
        
        return ans
                    


