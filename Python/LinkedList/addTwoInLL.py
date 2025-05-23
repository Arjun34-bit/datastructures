#reverse both linked list add them and reverse the output
class Node():
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



def addTwoLL(head1,head2):
    newHead1=head1
    newHead2=head2
    
    temp1=self.reverse(newHead1)
    temp2=self.reverse(newHead2)
    
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
            
    # print(carry)
        
    if carry != 0:
        newNode=Node(carry)
        temp=self.reverse(result.next)
        newNode.next=temp
        if newNode.data == 0:
            return newNode.next
        return newNode
        
    return self.reverse(result.next)
    
    
def traverseInLL(head):
    mover=head
    while mover:
        print(mover.data,end="->")
        mover=mover.next
    
    
    
    
sums=addTwoLL(head1,head2)
print(traverseInLL(sums))
        
        