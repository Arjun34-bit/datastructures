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


def reverseLL(head):
    current=head
    prev=None
    
    
    while current:
        nextNode=current.next
        current.next=prev   
        prev=current
        current=nextNode
        
        
    return prev


def isPalindrome(head):

    #learnt slow and fast pointer approach


    first=head
    
    slow=head
    fast=head
    
    while (fast.next != None and fast.next.next != None):  # finding the middle node TC:O(N/2)
        slow=slow.next
        fast=fast.next.next
        
        
    mid=slow.next
    
    newHead=reverseLL(mid)    #  reversing the second half TC:O(N/2)
    
    second=newHead
    
    while second != None:
        if first.data != second.data:
            reverseLL(newHead)       #  again reversing the second half TC:O(N/2) 
            return False           #  we need to rearrange the data structure if we altered the original data structure it is a good practice
            
        first=first.next
        second=second.next
        
    reverseLL(newHead)        #  again reversing the second half TC:O(N/2)
    return True


def insertInMiddle(head, x):        
    if head is None:
        return Node(x)
        
    if head.next is None:
        head.next=Node(x)
        return head
    
    slow=head
    fast=head
    
    while (fast.next != None and fast.next.next != None):
        slow=slow.next
        fast=fast.next.next
    
    key=Node(x)
    
    key.next=slow.next
    slow.next=key
    
    return head
        
arr=[15,2,3,4,5,6]
headVal=convertToLL(arr)
print("Searching for target element in Linked List ",searchInLL(headVal,6))
print("Traversing Linked List",end=" ")
print(traverseInLL(headVal))
print("Length of Linked List is ",lengthOfLL(headVal))
newNode=reverseLL(headVal)
print("Traversing Linked List after reversing")
print(traverseInLL(newNode))

newArr=[1,2,2,3]
palinLL=convertToLL(newArr)
print(f"Checking wheather a linked List {newArr} is palindrome or not :",isPalindrome(palinLL)) # Time Complexity is O(2N) and Space Complexity is O(1)
h=convertToLL([1,2,4])
print("Inserting key after middle",insertInMiddle(h,3))
# print(headVal)
