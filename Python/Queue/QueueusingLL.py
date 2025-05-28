class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    def __init__(self):
        self.head=None
        self.tail=None
    
    #Function to push an element into the queue.
    def push(self, item):
         #Add code here
        new_node=Node(item)
            
        if self.head == None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
            
        return self.head
    #Function to pop front element from the queue.
    def pop(self):
        if not self.head:
            return -1  
        popped_data = self.head.data
        self.head = self.head.next
        if not self.head:  
            self.tail = None
        return popped_data
        
        
obj=MyQueue()
head=obj.push(1)
head=obj.push(2)
head=obj.push(3)
head=obj.push(4)
head=obj.push(5)
head=obj.push(6)
print(obj.pop())
def traverseInLL(head):
    mover=head
    while mover:
        print(mover.data,end="->")
        mover=mover.next
print(traverseInLL(head))