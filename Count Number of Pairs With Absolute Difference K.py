from typing import Counter, List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        freq = Counter()
        
        for num in nums:
            # Check for complement pairs (num + k) and (num - k)
            print(freq[num-k])
            print(freq[num+k])
            a= freq[num - k]
            aw= freq[num + k]
            p=a+aw
            count+= p
            # Update the frequency of the current number
            freq[num] += 1
        
        return count
    
