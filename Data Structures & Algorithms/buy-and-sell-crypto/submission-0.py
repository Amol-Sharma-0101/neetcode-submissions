class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxn=0
        maxp=0
        for i in reversed(prices):
            maxn=max(maxn,i)
            maxp=max(maxp,maxn-i)
        return maxp
        