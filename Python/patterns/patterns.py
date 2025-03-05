class Patterns:
    def __init__(self,s):
        self.s=s

    def pattern1(self):
        print("Square")
        for i in range(self.s):
            for j in range(self.s):
               print("*",end=" ")
            print(end="\n")

    def pattern2(self):
        print("Right Angle triangle")
        for i in range(0,self.s+1):  #rows
            for j in range(0,i):  #columns
                print("*",end=" ")
                i+=1
            print(end="\n")

    def pattern3(self):
        print("Top Right Angle")
        for i in range(self.s,0,-1):
            for j in range(0,i):
                print("*",end=" ")
            print(end="\n")
            
    def pattern4(self):
        print("Left Right angle triangle")
        for i in range(1, self.s + 1):
            print(" " * (self.s - i), end="")
            for j in range(0,i):
                print("*",end="")
            print(end="\n")
            
    def pattern5(self):
        print("Triangle")
        for i in range(1, self.s + 1):
            print(" " * (self.s - i), end="")
            for j in range(0,i):
                print("*",end=" ")
            print(end="\n")


p1=Patterns(5)

p1.pattern1()
p1.pattern2()
p1.pattern3()
p1.pattern4()
p1.pattern5()