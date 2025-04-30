def findKNode(head,k):
    mover=head
    count=1
    
    while count<=k:
        mover=mover.next
        
    return mover

def reverseLLByKGroup(head,k):
    temp=head
    nextnode=None
    prevNode=None
    
    while temp != None:
        kNode=findKNode(temp,k)
        
        if kNode==None:
            if prevNode:
                prevNode.next=None
            break
        
        nextNode=kNode.next
        kNode.next=None
        
        reverse(temp)
        
        if temp==head:
            head=kNode
        else:
            prevNode.next=kNode
        
        prevNode=temp
        temp=nextNode