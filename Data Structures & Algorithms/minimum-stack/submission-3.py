class MinStack:

    def __init__(self):
        self.li=[]
        min=999999
    def push(self, val: int) -> None:
        return self.li.append(val)
        
        

    def pop(self) -> None:
        return self.li.pop()
        

    def top(self) -> int:
        return self.li[-1]
        

    def getMin(self) -> int:
        return min(self.li)

        
