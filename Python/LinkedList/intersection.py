#Partially done


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
        
def convertToLL(arr):
    head=Node(arr[0])
    mover=head
    
    for i in range(1,len(arr)):
        temp=Node(arr[i])
        mover.next=temp
        mover=temp
        
    return head
    
    
ll1=[4,4,4,4,4]
ll2=[4,4,4]
head1=convertToLL(ll1)
head2=convertToLL(ll2)


def intersection(head1,head2):
    mp={}
    
    temp=head1
    
    while temp:
        mp[temp]=True
        temp=temp.next
        
        
    temp=head2
    while temp != None:
        if mp[temp]:
            return temp.data
        temp=temp.next
        
    return -1
        
        
print(intersection(head1,head2))