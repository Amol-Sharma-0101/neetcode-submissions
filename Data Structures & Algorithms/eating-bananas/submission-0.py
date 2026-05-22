class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L=1
        R=max(piles)
        res=R
        while L<=R:
            k=(L+R)//2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(float(pile)/k)
            if total_hours<=h:
                res=k
                R=k-1
            else:
                L=k+1
        return res

        