class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        N=0
        while N+2<len(nums) and nums[N]<=0:
            if N > 0 and nums[N] == nums[N-1]:
                N+=1
                continue
            L=N+1
            R=len(nums)-1
            while(L<R):
                cursum=nums[N]+nums[L]+nums[R]
                if cursum==0:
                    ans.append([nums[N],nums[L],nums[R]])
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1
                    L += 1
                    R -= 1
                elif cursum<0:
                    L+=1
                elif cursum>0:
                    R-=1
            
            N+=1

        return ans