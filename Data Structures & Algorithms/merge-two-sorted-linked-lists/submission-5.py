# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        h1=list1
        h2= list2
        list1=[]
       
        while h1!=None or h2!=None:
            if h1:
                list1.append(h1.val)
                h1=h1.next
            if h2:
                list1.append(h2.val)
                h2=h2.next

        list1.sort()
        if list1:
            head=ListNode(list1[0])
        else:
            head = None
        curr=None
        prev=head
        for i in range(1, len(list1)):
            curr= ListNode(list1[i])
            prev.next=curr
            prev = curr

        return head
            

            



        return list1