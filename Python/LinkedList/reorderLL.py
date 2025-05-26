def reverse(self,head):
    curr=head
    prev=None
    
    while curr:
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp
        
    return prev
    
def reorderList(self, head):
    # code here
    
    temp=head
    
    slow=temp
    fast=temp
    
    while fast.next != None and fast.next.next != None:
        slow=slow.next
        fast=fast.next.next
        
    # middle node is slow
    
    second_half=self.reverse(slow.next)
    slow.next=None
    
    first_half = temp
    while second_half:
        temp1 = first_half.next
        temp2 = second_half.next

        first_half.next = second_half
        second_half.next = temp1

        first_half = temp1
        second_half = temp2
        
    return first_half
    
    