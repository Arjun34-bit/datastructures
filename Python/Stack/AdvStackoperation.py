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
s.push(10)
s.push(20)
s.push(30)
s.push(40)

s.pop()

print("Peek Element in Stack",s.peek())
print("Minimum Element in Stack",s.getMin())