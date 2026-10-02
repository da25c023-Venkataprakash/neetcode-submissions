class Node:
    def __init__(self,val=0, next_node= None):
        self.val=val
        self.next= next_node




class MyLinkedList:

    def __init__(self):
        self.head=Node()
        self.size = 0
        self.tail=self.head
        

    def get(self, index: int) -> int:
        if index >= self.size or index<0:
            return -1
        else:
            curr = self.head.next
            for i in range(index):
                curr=curr.next
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        new= Node(val)
        old = self.head.next
        new.next = old
        self.head.next = new
        if self.size==0:
            self.tail = new
     
        self.size+=1
        
        

    def addAtTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next
        self.size+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        new= Node(val)
        if index<=self.size:
            curr = self.head
            for i in range(index):
                curr=curr.next
            add= curr.next
            new.next = add
            curr.next = new
            if index == self.size:
                self.tail=new
            self.size+=1

        

    def deleteAtIndex(self, index: int) -> None:
        if index< 0 or index >=self.size:
            return 
        
        curr = self.head.next
        for i in range(index-1):
            curr=curr.next
        new=curr.next.next
        curr.next = new
        if index == self.size - 1: 
            self.tail = curr
        self.size-=1


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)