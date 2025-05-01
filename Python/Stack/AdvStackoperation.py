class Stack:
    def __init__(self):
        self.arr=[]
        self.mini=[]
        
    def push(self, x):
        
        self.arr.append(x)
        
        if not self.mini or x<=self.mini[-1]:
            self.mini.append(x)
        else:
            self.mini.append(self.mini[-1])

    def pop(self):
        if len(self.arr)==0:
            return -1
        poped=self.arr.pop()
        self.mini.pop()
        return poped

    def peek(self):
        if len(self.arr)==0:
            return -1
        return self.arr[-1]

    def getMin(self):
        if len(self.arr)==0:
            return -1
        return self.mini[-1]
    

s=Stack()