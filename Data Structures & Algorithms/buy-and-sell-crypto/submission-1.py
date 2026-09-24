class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxi=0
        max
        for i in range (n):
            a=prices[i]
            sell=max(prices[i:n])
            maxi=max(maxi, sell-a)
        return maxi
        