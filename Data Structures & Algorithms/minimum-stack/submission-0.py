class MinStack:

    def __init__(self):
        self.stack=[]
        # self.minn=(2^31 - 1)

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
