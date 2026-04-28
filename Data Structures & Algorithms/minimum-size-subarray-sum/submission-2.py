class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        minLen=n+1
        total=L=0
        for R in range(n):
            total+=nums[R]
            while total>=target:
                minLen=min(R-L+1,minLen)
                total-=nums[L]
                L+=1
        return minLen if minLen!=n+1 else 0