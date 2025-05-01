class TwoStacks:
    def __init__(self):
        self.arr1=[]
        self.arr2=[]

    def push1(self, x):
        self.arr1.append(x)
        pass

    def push2(self, x):
        self.arr2.append(x)
        pass

    def pop1(self):
        if len(self.arr1)==0:
            return -1
        poped=self.arr1.pop()
        return poped

    def pop2(self):
        if len(self.arr2)==0:
            return -1
        poped=self.arr2.pop()
        return poped
    


s=TwoStacks()    #TC : O(1) and SPC : O(1)
s.push1(10)
s.push1(20)
s.push2(30)
s.push2(40)

print(s.pop1())
print(s.pop2())