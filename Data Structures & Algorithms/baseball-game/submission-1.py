class Solution:
    def calPoints(self, operations: List[str]) -> int:
        n=len(operations)
        stack=[]
        score=0
        for i in range(n):
            if operations[i]=='+':
                stack.append(stack[-1]+stack[-2])
                score+=stack[-1]
            elif operations[i]=='D':
                stack.append(2*stack[-1])
                score+=stack[-1]
            elif operations[i]=='C':
                score-=stack[-1]
                stack.pop()
            else:
                stack.append(int(operations[i]))
                score+=stack[-1]
        return score
