class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=len(nums)
        minLen=l+1
        lsum=0
        L=0
        for R in range(l):
            lsum+=nums[R]
            while lsum>=target:
                minLen=min((R-L+1),minLen)
                lsum-=nums[L]
                L+=1
        return minLen if minLen!=l+1 else 0