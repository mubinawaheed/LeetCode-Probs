# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def strStr( haystack: str, needle: str) -> int:
    if(len(haystack)<len(needle)):
        return -1
    i=0
    j=0
    startingIndex=-1
    while j<len(needle) and i<len(haystack):
        if(haystack[i] != needle[j]):
            

            if(j>0):
                j=0
            if(startingIndex>=0):
                
                i=startingIndex+1
                startingIndex=-1
            else:
                i+=1
                startingIndex=-1
        elif(haystack[i]==needle[j]):

            if(startingIndex<0):
                startingIndex=i
            i+=1
            j+=1
            
    if(startingIndex>0):
        if(j<len(needle)):
            return -1
    return startingIndex


s='aabaaabaaac'
a=strStr(s, 'aabaaac')
print(a)