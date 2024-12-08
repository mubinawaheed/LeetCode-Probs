
def f():
    s=[]
    t=[]
    start="_L__R__R_"
    target="L______RR"
    for j in range(len(start)):
        s.append(start[j])
        t.append(target[j])


    for i in range(len(start)):
        isSwaped=False
        if(s[i]=='L'):
            if(i>0 and s[i-1]=='_'):
                s[i], s[i-1] = s[i-1], s[i]
                isSwaped=True

        if(i+1<len(s) and s[i]=='R' and s[i+1]=='_'):
            s[i+1], s[i] = s[i], s[i+1]
            isSwaped=True
            
        if(isSwaped):
            flag  = all(x == y for x, y in zip(s,t))
            if(flag):
                return True
    print(s)
    return False

answer = f()
def canChange(start, target):
    s={}
    t={}
    for i in range(len(target)):
        if(target[i]=='L' or target[i]=='R'):
            s[i]=target[i]
    print(s)
start="_L__R__R_"
target="L______RR"   
canChange(start,target)


