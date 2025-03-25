from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int: #optimized
        meetings.sort()
        prev=-1
        for start, end in meetings:
            start = max(start, prev+1)
            l=end-start+1
            days -=max(l,0)
            prev=max(prev, end)
        return days

        
        #-----------my code-----------------#
        
        # meeting_days=[]

        # for s, e in meetings:
        #     if s<=prev:
        #         meeting_days[-1][1] = max(meeting_days[-1][1] ,e)
        #     else:
        #         meeting_days.append([s,e])
        #     prev= max(prev, e)

        # count = 0
        # for i, j in meeting_days:
        #     k= j-i+1
        #     count+=k

        # return days-count

        
