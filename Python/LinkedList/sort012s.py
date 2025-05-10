def seggregate(head):   #Brute Force Approach   TC: O(2N) and SC: O(1)
    temp=head
    temp1=head
    count0=0
    count1=0
    count2=0
    
    while temp != None:
        if temp.data==0:
            count0+=1
        elif temp.data==1:
            count1+=1
        else:
            count2+=1
        temp=temp.next
        
    while temp1 != None:
        if count0:
            temp1.data=0
            count0-=1
        elif count1:
            temp1.data=1
            count1-=1
        else:
            temp1.data=2
            count2-=1
        temp1=temp1.next
    
    return head


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def segregate(head):   # TC:O(N) and SC:O(1)
    temp=head
    
    zeroHead=Node(-1)
    oneHead=Node(-1)
    twoHead=Node(-1)
    
    zero=zeroHead
    one=oneHead
    two=twoHead
    
    while temp != None:
        if temp.data==0:
            zero.next=temp
            zero=temp
        elif temp.data==1:
            one.next=temp
            one=temp
        else:
            two.next=temp
            two=temp
        temp=temp.next
        
        
    if(oneHead.next != None):
        zero.next=oneHead.next
    else:
        zero.next=twoHead.next
        
    one.next=twoHead.next
    
    two.next=None
    
    return zeroHead.next