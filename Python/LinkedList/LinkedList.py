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
    
        
arr=[15,2,3,4,5,6]
headVal=convertToLL(arr)
print(headVal)