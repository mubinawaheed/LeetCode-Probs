from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        k=strs[0]
        c=''
     
        for i in range(1, len(strs)):
            a=strs[i]
            m=0
            while m<len(a) and m<len(k) and a[m] == k[m]:
                c+=a[m]
                m+=1
            if len(c) ==0:
                return ''
            k=c
            c=''
        return k