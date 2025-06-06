def findLoop(head):    #TC:O(N) and SC:O(N)
    temp=head
    
    mp={}
    
    while temp != None:
        if temp in mp:
            return True
        
        mp[temp]=1
            
        temp=temp.next
        
    return False
    
    
def detectLoop(head):    #TC:O(N) and SC:O(1)
    slow=head
    fast=head
    
    while fast != None and fast.next != None:
            
        slow=slow.next
        fast=fast.next.next

        if slow==fast:
            return True
        
    return False