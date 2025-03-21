import sys

def maxSubArraySum(arr):
    n=len(arr)
    maxi=-sys.maxsize-1
    sums=0
    
    for i in range(0,len(arr)):
        sums+=arr[i]
        if sums>maxi:
            maxi=sums
        if sums<0 and i<n-1:
            sums=0
    return maxi  
    
arr=[-2,-4]
print(maxSubArraySum(arr))
