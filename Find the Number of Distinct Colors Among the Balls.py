from collections import defaultdict
from typing import List
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        mp = {}  # Maps ball -> color
        color_count = defaultdict(int)  # Maps color -> count of balls with that color
        res = []
        distinct_colors = 0  # Tracks the number of distinct colors

        for a, b in queries:
            if a in mp:  # If ball 'a' already has a color
                old_color = mp[a]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:  # If no balls use this color anymore
                    distinct_colors -= 1

            # Assign new color
            mp[a] = b
            if color_count[b] == 0:  # If this is the first ball with this color
                distinct_colors += 1
            color_count[b] += 1

            res.append(distinct_colors)

        return res

q=Solution()
l=q.queryResults(4,[[0,1],[1,4],[1,1],[1,4],[1,1]])