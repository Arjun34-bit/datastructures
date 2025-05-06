def findLoop(head):    #TC:O(N) and SC:O(N)
    temp=head
    
    mp={}
    
    while temp != None:
        mp[temp]=1
        
        if temp in mp:
            return True
            
        temp=temp.next
        
    return False
    
    
def detectLoop(head):    #TC:O(N) and SC:O(1)
    slow=head
    fast=head
    
    while slow.next.next != None or fast.next != None:
        
        if slow==fast:
            return True
            
        slow=slow.next
        fast=fast.next
        
    return False