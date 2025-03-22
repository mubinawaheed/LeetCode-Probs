from collections import defaultdict
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        res=0
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        visited= set()
        def dfs(v, res):
            if v in visited:
                return 
            res.append(v)
            visited.add(v)
            for nei in adj[v]:
                dfs(nei, res)

            return res

        for i in range(n):
            if i in visited:
                continue
            components = dfs(i, [])
            if all([len(components)-1 == len(adj[c]) for c in components ]):
                res+=1

        return res