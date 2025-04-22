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



def searchInLL(head,target):
    mover=head

    while mover:
        
        if(mover.data == target):
            return True
        else:
            mover=mover.next
            
    return False
    
    
def traverseInLL(head):
    mover=head
    while mover:
        print(mover.data,end="->")
        mover=mover.next
        
        
def lengthOfLL(head):
    mover=head
    count=0
    while mover:
        count+=1
        mover=mover.next
        
    return count
        
arr=[15,2,3,4,5,6]
headVal=convertToLL(arr)
print("Searching for target element in Linked List ",searchInLL(headVal,6))
print("Traversing Linked List",end=" ")
print(traverseInLL(headVal))
print("Length of Linked List is ",lengthOfLL(headVal))
# print(headVal)
