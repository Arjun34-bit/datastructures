class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


arr=[1,2,3,4,5,6]

def LL(arr):
    head=Node(arr[0])
    mover=head
    
    for i in range(1,len(arr)):
        temp=Node(arr[i])
        mover.next=temp
        mover=temp
        

    return head

newHead=LL(arr)



def pairWiseSwap(head):
    temp=head
        
    while (temp != None and temp.next != None):
        
        temp1=temp.data
        temp.data=temp.next.data
        temp.next.data=temp1
        
        temp=temp.next.next
        
    return head


def traverseInLL(head):
    mover=head
    while mover:
        print(mover.data,end="->")
        mover=mover.next


h=pairWiseSwap(newHead)
print(traverseInLL(h))