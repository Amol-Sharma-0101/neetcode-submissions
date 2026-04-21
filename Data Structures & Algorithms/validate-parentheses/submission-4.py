class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        array=list(s)
        for i in array:
            if i in '[({':
                stack.append(i)
            elif i==')':
                if not stack:
                    return False
                elif stack[-1]=='(':
                    stack.pop()
                else:
                    return False
            elif i=='}':
                if not stack:
                    return False
                elif stack[-1]=='{':
                    stack.pop()
                else:
                    return False
            elif i==']':
                if not stack:
                    return False
                elif stack[-1]=='[':
                    stack.pop()
                else:
                    return False
        return True if not stack else False