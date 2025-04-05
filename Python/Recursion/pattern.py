class Solution:
    def __init__(self):
        self.result=[]
        
    def pattern1(self,n):
        if n>self.result[0]:
            return
        self.result.append(n)
        # print(n,end=" ")
        self.pattern1(n+5)
               
    def pattern(self, n):
        # code here
        self.result.append(n)
        # print(n,end=" ")
        if n<=0:
            self.pattern1(n+5)
            return self.result
        self.pattern(n-5)
        return self.result
    




obj=Solution()
print(obj.pattern(16))