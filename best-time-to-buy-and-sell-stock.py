from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = min(prices)
        dayToBuy = prices.index(lowestPrice)
        if(dayToBuy == len(prices)-1):
            return 0
        else:
            highestPrice = max(prices[dayToBuy:])
            dayToSell = prices[dayToBuy:].index(highestPrice)
            return highestPrice-lowestPrice