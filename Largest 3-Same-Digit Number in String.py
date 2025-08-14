class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res=int(num[0])
        count=1
        ans={}
        for i in range(1,len(num)):
            if count == 3:
                if (int(res)<= int(num[i])):
                    ans[res]=3
                    res = int(num[i])
                    count=1
            elif count<3 and res != int(num[i]):
                count=1
                res=int(num[i])
            elif int(num[i]) == res:
                count+=1
                if count == 3:
                    if (int(res)<= int(num[i])):
                        ans[res]=3
                        res = int(num[i])
                        count=1
               

        sorted_dict = dict(sorted(ans.items(), key=lambda x: x[0], reverse=True))
        print(sorted_dict)
        for k , v in sorted_dict.items():
            return str(k)*v
        if count == 3:
            return str(res)*3
        return ''
    class Solution:
        def largestGoodInteger(self, num: str) -> str:
            for i in range(9, -1,-1):
                if str(i)*3 in num:
                    return str(i)*3

            return ''