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
        

def intersectPoint(head1, head2):      #return value will be None may be because of address changing         
    if(head1==None and head2==None):
        return None
        
    temp1=head1
    temp2=head2
    
    while (temp1 != temp2):
        temp1=temp1.next
        temp2=temp2.next
        
        if(temp1==temp2):
            return temp1
            
        if(temp1==None):
            temp1=head2
            
        if(temp2==None):
            temp2=head1
            
    return temp1
        
def union(head1,head2):
    s1=set()
    s2=set()
    
    temp1=head1
    temp2=head2
    
    while temp1:
        s1.add(temp1.data)
        temp1=temp1.next
        
    while temp2:
        s2.add(temp2.data)
        temp2=temp2.next
        
        
        
    u=s1.union(s2)
    u_list=list(u)
    
    u_list.sort()
    
    newHead=Node(u_list[0])
    mover=newHead
    
    for i in range(1,len(u_list)):
        temp=Node(u_list[i])
        mover.next=temp
        mover=temp
        
    return newHead

# print(intersection(head1,head2))
print(intersectPoint(head1,head2))     #TC:O(n1+n2)  SC:O(1)