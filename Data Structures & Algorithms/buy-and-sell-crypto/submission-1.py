class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn= float('inf') 
        maxp=0
        for i in prices:
            minn=min(minn,i)
            maxp=max(maxp,i-minn)
        return maxp