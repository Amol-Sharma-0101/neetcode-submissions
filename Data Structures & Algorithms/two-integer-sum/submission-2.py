class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in hashmap:
                return [hashmap[diff][0],i]
            if n not in hashmap:
                hashmap[n]=[i]
            else:
                hashmap[n].append(i)