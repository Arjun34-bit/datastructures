def findFirstNode(head):
    temp=head
    
    mp={}
    
    while temp != None:
        mp[temp]=1
        
        if temp in mp:
            return temp
            
        temp=temp.next
        
    return None
    
    
def findStartingPoint(head):
    slow=head
    fast=head
    
    while fast != None and fast.next != None:
        slow=slow.next
        fast=fast.next.next
        
        if slow==fast:
            slow=head
            
            while slow != fast:
                slow=slow.next
                fast=fast.next
            return slow
            
    return None