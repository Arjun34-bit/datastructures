def countNodesInLoop(self, head):
    temp=head

    mp={}
    
    d=1
    
    while temp != None:
        
        if temp in mp:
            value=mp[temp]
            return d-value
        
        mp[temp]=d
        
        d+=1
        temp=temp.next
        
    return 0
    
def findLength(slow,fast):
    count=1
    fast=fast.next
    
    while slow != fast:
        count+=1
        fast=fast.next
    return count

    
def findLoop(head):
    temp=head
    
    slow=temp
    fast=temp
    
    while fast != None and fast.next != None:
        slow=slow.next
        fast=fast.next.next
        
        if slow==fast:
            return findLength(slow,fast)
            
    return 0