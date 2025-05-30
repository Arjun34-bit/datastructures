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
