class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapp={')':'(','}':'{',']':'['}
        array=list(s)
        for i in array:
            if i in mapp:
                if stack and stack[-1]==mapp[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False