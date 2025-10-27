class Stack:
    def __init__(self):
        self.top = -1
        self.st = []

    def push(self,data):
        self.top += 1
        self.st.append(data)
        return self.st
    
    def pop(self):
        if(self.top == -1):
            return "Stack is empty"
        self.top -= 1
        return self.st[self.top + 1]
    
    def peek(self):
        if(self.top == -1):
            return "Stack is empty"
        return self.st[self.top]
    
    def size(self):
        return self.top + 1
    
    def print(self):
        if(self.top == -1):
            return "Stack is empty"
        for i in range(0, self.top + 1):
            print(self.st[i], end=" ")
    

stackImpl = Stack()
stackImpl.push(10)
stackImpl.push(20)
stackImpl.push(30)
stackImpl.push(40)

print(f"Stack elements: {stackImpl.print()}")

print(stackImpl.peek())


print(f"Stack elements: {stackImpl.print()}")

print(stackImpl.pop())

print(f"Stack elements: {stackImpl.print()}")

stackImpl.peek()

print(f"Stack Size : {stackImpl.size()}")

print(f"Stack elements: {stackImpl.print()}")


    