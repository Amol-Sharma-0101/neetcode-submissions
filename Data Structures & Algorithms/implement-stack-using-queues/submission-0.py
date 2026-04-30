class MyStack:

    def __init__(self):
        self.q1=[]
        self.q2=[]

    def push(self, x: int) -> None:
        while len(self.q1)!=0:
            self.q2.append(self.q1.pop(0))
        self.q1.append(x)
        while len(self.q2)!=0:
            self.q1.append(self.q2.pop(0))

    def pop(self) -> int:
        return self.q1.pop(0)

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return False if len(self.q1)!=0 else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()