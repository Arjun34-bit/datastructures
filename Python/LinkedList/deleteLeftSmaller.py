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