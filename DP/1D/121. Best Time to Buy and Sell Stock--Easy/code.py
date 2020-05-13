#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
prices=[7,1,5,3,6,4]

#DP O(N)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest=10e8
        maxProfit=0
        curProfit=0
        for price in prices:
            curProfit=price-lowest
            maxProfit=max(curProfit,maxProfit)
            lowest=min(lowest,price)
        return maxProfit