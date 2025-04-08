
# Time and Space Complexity is O(n)

class Solution:
    def __init__(self):
        self.result=[]
        
    def pattern1(self,n):
        if n>self.result[0]:
            return
        self.result.append(n)
        self.pattern1(n+5)
               
    def pattern(self, n):
        self.result.append(n)
        if n<=0:
            self.pattern1(n+5)
            return self.result
        self.pattern(n-5)
        return self.result
    




obj=Solution()
print(obj.pattern(16))