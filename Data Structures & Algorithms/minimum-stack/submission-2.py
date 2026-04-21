class MinStack:

    def __init__(self):
        self.stack=[]
        self.minn=(2^31 - 1)

    def push(self, val: int) -> None:
        if not self.stack:
            self.minn=val
            self.stack.append(0)
        else:
            self.stack.append(val-self.minn)
            if val<self.minn:
                self.minn=val
                

    def pop(self) -> None:
        if not self.stack:
            return
        pop=self.stack.pop()
        if pop<0: #means popping this element will change the minimum i.e. this element was the new minimum
            self.minn=self.minn-pop

    def top(self) -> int:
        top = self.stack[-1]
        if top>0: # this means that the top of the stack is not the min value, we have to add the difference to the current min in order to get this top value
            return top+self.minn
        else: #this means that the top is the current min, so we can just return min
            return self.minn

    def getMin(self) -> int:
        return self.minn
