class LinkedList:
    
    def __init__(self):
      self.head = ListNode(-1)
      self.tail = self.head
        

    
    def get(self, index: int) -> int:
        curr=self.head.next
        i=0
        while(curr and i<index):
            curr=curr.next
            i+=1
        return curr.value if curr else -1

        

    def insertHead(self, val: int) -> None:
        node = ListNode(val)
        node.next=self.head.next
        self.head.next = node
        
        if self.head == self.tail:
            self.tail = node
        
        

    def insertTail(self, val: int) -> None:
        node =ListNode(val)
        self.tail.next=node
        self.tail = node


    def remove(self, index: int) -> bool:
        curr=self.head
        i=0
        while (curr and i<index):
            curr=curr.next
            i+=1

        if curr and curr.next:
            noderemove = curr.next
            curr.next = noderemove.next
            if noderemove == self.tail:
                self.tail = curr

            return True
        return False

        

        

    def getValues(self) -> List[int]:
        lists=[]
        curr=self.head.next
        while(curr!=None):
            lists.append(curr.value)
            curr=curr.next
        return lists 
        


class ListNode:
    def __init__(self,val):
        self.value= val
        self.next = None