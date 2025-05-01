class MyStack:
    def __init__(self):
        self.arr=[]
    
    def push(self,data):
        self.arr.append(data)
        return True
    
    def pop(self):
        if len(self.arr)==0:
            return -1
        poped=self.arr.pop()
        return poped
    


s=MyStack()    #TC : O(1) and SPC : O(1)
s.push(10)
s.push(20)
s.push(30)

print(s.pop())