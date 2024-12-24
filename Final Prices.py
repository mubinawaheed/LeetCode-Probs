class Solution:
    def finalPrices(self, prices):
        answers=[]
        for i in range(len(prices)-1):
            k = prices[i]
            j=i+1
            while j<len(prices) and prices[j]>k :
                j+=1
            if(j<len(prices) and prices[j]<=k):
                answers.append(k-prices[j])
            else:
                answers.append(prices[i])
        answers.append(prices[-1])

        return answers
            

        