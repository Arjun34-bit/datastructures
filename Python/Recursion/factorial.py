#Time Complexity : O(n)
#Space Complexity : O(1)

def factorial(sums,n):
    if n==0:
        return sums
    sums=sums*n
    n-=1
    val=factorial(sums,n)
    return val
    
def main(n):
    sums=1
    result=factorial(sums,n)
    return result
    
print(main(5))