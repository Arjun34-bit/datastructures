#reverse both linked list sub them and reverse the output
class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        
def negZero(head):
    temp=head
    
    while temp.data == 0:
        temp=temp.next
        
    return temp

        
def getLength(Node):
    size = 0
    while (Node != None):
    
        Node = Node.next
        size = size + 1
    
    return size
        
def convertToLL(arr):
    head=Node(arr[0])
    mover=head
    for i in range(1,len(arr)):
        temp=Node(arr[i])
        mover.next=temp
        mover=temp
        
    return head
    
arr1=[6,3]
arr2=[7,1,0]

head1=convertToLL(arr1)
head2=convertToLL(arr2)


def reverse(head):
    curr=head
    prev=None
    
    while curr:
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp
        
    return prev


def subLinkedList(head1, head2): 
    temp1=head1
    temp2=head2
    
    l1=getLength(temp1)
    l2=getLength(temp2)
    
    if l1 != l2:
        if l1 > l2:
            rHead1=reverse(temp1)
            rHead2=reverse(temp2)
        else:
            rHead1=reverse(temp2)
            rHead2=reverse(temp1)
            
    else:
        rHead1=reverse(temp1)
        rHead2=reverse(temp2)
    
    # print(rHead2.data)
    
    borrow=0
    
    result=Node(-1)
    ans=result
    
    while rHead1 != None or rHead2 != None:
        sub=0
        d1=0
        d2=0
        if rHead1:
            d1=rHead1.data
        if rHead2:
            d2=rHead2.data
        # print(rHead2.data)
        sub=d1 - d2 - borrow
        
        if sub < 0:
            sub += 10
            borrow=1
        else:
            borrow=0
        
        node=Node(sub)
        ans.next=node
        ans=node
        
        if rHead1:
            rHead1=rHead1.next
        if rHead2:
            rHead2=rHead2.next
            
    revResult=reverse(result.next)
    return negZero(revResult)
    
def traverseInLL(head):
    mover=head
    while mover:
        print(mover.data,end="->")
        mover=mover.next
    
    
    
    
sums=subLinkedList(head1,head2)
print(traverseInLL(sums))
        
        