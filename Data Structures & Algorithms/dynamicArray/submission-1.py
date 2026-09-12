class DynamicArray:
    
    def __init__(self, Capacity: int):
        self.Capacity = Capacity
        self.length = 0
        self.array = [0] * Capacity

    def get(self, i: int) -> int:
        return self.array[i]


    


    def pushback(self, n: int) -> None:
        if self.length == self.Capacity:
            self.resize()

        self.array[self.length]=n
        self.length+=1

    def set(self, i: int, n: int) -> None:
        self.array[i]=n

    def popback(self) -> int:
        a= self.array[self.length-1]
        self.length-=1
        return a
 

    def resize(self) -> None:
        self.Capacity = 2*self.Capacity
        
        self.newarray= [0]*self.Capacity

        for i in range(self.length):
            self.newarray[i] = self.array[i]
        
        self.array= self.newarray




    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.Capacity
