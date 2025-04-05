
# Time Complexity is O(n)

# We can reduce this by dividing the n by 2 i.e making them half at each step
class Solution:
    def reverse(self,n):
        temp=0
        while n>0:
            rev=n%10
            temp=temp*10+rev
            n=n//10
        return temp
    
    def power(self,x,n):
        if n==0:
            return 1
        half=self.power(x,n//2)
        if n%2==0:
            return half*half
        else:
            return x*half*half
    def reverse_exponentiation(self, n):
        rev=self.reverse(n)
        
        return self.power(n,rev)
    


obj=Solution()

print(obj.reverse_exponentiation(5))