#reverse both linked list add them and reverse the output
class Node():
    def __init__(self,data):
        self.data=data
        self.next=None


def negZero(head):
        while head and head.data == 0:
            head = head.next
        return head

def convertToLL(arr):
    head=Node(arr[0])
    mover=head
    for i in range(1,len(arr)):
        temp=Node(arr[i])
        mover.next=temp
        mover=temp
        
    return head
    
arr1=[4,5]
arr2=[3,4,5]

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



def addTwoLL(num1,num2):
    newHead1=num1
    newHead2=num2
    
    temp1=reverse(newHead1)
    temp2=reverse(newHead2)
    
    result=Node(-1)
    ans=result
    
    carry=0
    
    while temp1 or temp2 :
        if temp1 == None:
            sums=Node(temp2.data)
        elif temp2 == None:
            sums=Node(temp1.data)
        else:
            sums=Node(temp1.data + temp2.data + carry)
        
        node=Node(sums.data % 10)
        
        if sums.data < 10:
            ans.next=node
            ans=node
            carry=0
        else:
            ans.next=node
            ans=node
            carry=(sums.data // 10)
        
        if temp1:
            temp1=temp1.next
        if temp2:
            temp2=temp2.next
            
    if carry != 0:
        newNode=Node(carry)
        temp=reverse(result.next)
        newNode.next=temp
        return negZero(newNode)
        
        
    revResult=reverse(result.next)
    return negZero(revResult)  
    
def traverseInLL(head):
    mover=head
    while mover:
        print(mover.data,end="->")
        mover=mover.next
    
    
    
    
sums=addTwoLL(head1,head2)
print(traverseInLL(sums))
        
        