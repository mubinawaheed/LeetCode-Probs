from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        num_set=set(arr)
        max_len=0

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                prev=arr[j]
                curr = arr[i] + arr[j]
                curr_len=2

                while curr in num_set:
                    prev, curr = curr, curr + prev

                    curr_len+=1
                    max_len=max(curr_len, max_len)
        return max_len
arr = [1,3,7,11,12,14,18]
s=Solution()
s.lenLongestFibSubseq(arr)