from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        rem={}
        folders=sorted(folder)
        for i in range(len(folders)):
            if folders[i] in rem:
                continue
            for j in range(i+1, len(folders)):
                if folders[j].startswith(folders[i]+'/'):
                    rem[folders[j]]=True
                
        res=[]
        for k in folders:
            if k not in rem:
                res.append(k)
        return res