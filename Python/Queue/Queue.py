class MyQueue:
    def __init__(self):
        self.q=[]
    
    #Function to push an element x in a queue.
    def push(self, x):
         
         #add code here
         self.q.append(x)
     
    #Function to pop an element from queue and return that element.
    def pop(self):
        if len(self.q) == 0:
            return -1
        popped=self.q.pop(0)
        return popped
         # add code here


#From Queue Collection
from queue import Queue


def push(x):

    global queue_1
    global queue_2
    # code here
    
    queue_2.put(x)
    
    while not queue_1.empty():
        queue_2.put(queue_1.get())
        
    queue_1,queue_2=queue_2,queue_1


def pop():

    global queue_1
    global queue_2
    
    if not queue_1.empty():
        return queue_1.get()
    return -1