from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        s = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if digits == '':
            return []
        def recurse(num, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            ltrs = s[digits[num]]
            for k in ltrs:
                recurse(num+1, curStr+k)


        res=[]
        recurse(0,'')

        return res

