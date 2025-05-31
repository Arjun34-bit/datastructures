def compute(head):
    temp=head
    rHead=temp
    prev=None
    curr=None
    
    if temp.data < temp.next.data:
        rHead=rHead.next
    
    while temp != None and temp.next != None:
        currNode=temp.data          #16  15
        nextNode=temp.next.data     #15  19
        # print(currNode)
        # print(nextNode)
        if currNode < nextNode:
            curr=temp.next               #19
            if prev:
                prev.next=curr              #19
            prev=curr
        else:
            prev=temp           #16
            
        temp=temp.next          #15
        
    return rHead


class Solution:
    def reverse(self,head):
            curr=head
            prev=None
            
            while curr:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
                
            return prev
        
    def compute(self,head):
        #Your code here
        
        rHead=self.reverse(head)
        
        
        max_so_far = rHead.data
        curr = rHead
        while curr and curr.next:
            if curr.next.data < max_so_far:
                curr.next = curr.next.next
            else:
                curr = curr.next
                max_so_far = curr.data
                

        return self.reverse(rHead)