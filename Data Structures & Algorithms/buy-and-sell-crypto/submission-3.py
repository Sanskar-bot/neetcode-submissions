class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxi=0
        max
        for i in range (n):
            a=prices[i]
            for j in range (i ,n):
                b=prices[j]
                maxi=max(maxi, b-a)
        return maxi
        