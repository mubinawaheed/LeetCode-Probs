class Solution:
    def sortVowels(self, s: str) -> str:
        res=[]
        vowels={'a': True, 'e': True, 'i': True, 'o': True, 'u': True,'A': True, 'E': True, 'I': True, 'O': True, 'U': True   }
        f=[]

        for i in s:
            if i in vowels:
                res.append('')
                f.append(i)
            else:
                res.append(i)

        f.sort(reverse=True)   # in-place descending
        for k in range(len(res)):
            if len(f) == 0:
                break
            if res[k]=='':
                l=f.pop()
                res[k]=l



        return ''.join(res)