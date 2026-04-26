class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashmap={}
        for i in s:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        for j in t:
            if j not in hashmap:
                return False
            else:
                if hashmap[j]==0:
                    return False
                else:
                    hashmap[j]-=1
        for x in hashmap:
            if hashmap[x]!=0:
                return False
        return True
                