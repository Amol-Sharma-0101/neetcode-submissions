class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxnum=-1
        for i in reversed(range(len(arr))):
            temp=arr[i]
            arr[i]=maxnum
            maxnum=max(temp,maxnum)
        arr[-1]=-1
        return arr
        