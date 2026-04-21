class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        score=0
        for i in operations:
            if i=='+':
                stack.append(stack[-1]+stack[-2])
                score+=stack[-1]
            elif i=='D':
                stack.append(2*stack[-1])
                score+=stack[-1]
            elif i=='C':
                score-=stack[-1]
                stack.pop()
            else:
                stack.append(int(i))
                score+=stack[-1]
        return score
