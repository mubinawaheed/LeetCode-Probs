# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

a = [9,1,2,4]

def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    if (digits[-1] == 9):
       
        i=len(digits)-1
        while (digits[i]==9):
            digits[i]=0
            i-=1
        if(i>=0):    
            digits[i]+=1
        else:
            digits.insert(0, 1)
    else:
        digits[-1]+=1
    return digits

plusOne(a)
print(a)