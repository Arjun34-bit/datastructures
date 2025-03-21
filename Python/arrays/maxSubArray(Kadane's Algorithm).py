import sys
def maxSubArraySum( arr):
    # Your code here
    n=len(arr)
    maxi=-sys.maxsize-1
    
    sums=0
    
    for i in range(0,n):
        sums+=arr[i]
        
        if sums>maxi:
            maxi=max(maxi,sums)
            
        if sums<0 and i<n-1:
            sums=0
    return maxi

arr=[-2,-4]
print(maxSubArraySum(arr))