class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            maxnum=0
            for j in range(i+1,len(arr)):
                maxnum=max(arr[j],maxnum)
            arr[i]=maxnum
        arr[-1]=-1
        return arr
        