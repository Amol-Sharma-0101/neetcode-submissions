class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in hashmap:
                return [hashmap[diff][0],i]
            if nums[i] not in hashmap:
                hashmap[nums[i]]=[i]
            else:
                hashmap[nums[i]].append(i)