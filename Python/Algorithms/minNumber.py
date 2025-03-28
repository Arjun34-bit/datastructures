import sys
def minNumber(arr,low,high):
        #Your code here
        
    minVal=sys.maxsize
    
    while low<=high:
        mid=low+(high-low)//2
        
        if arr[low]<=arr[mid]:
            minVal=min(minVal,arr[low])
            low=mid+1
        else:
            minVal=min(minVal,arr[mid])
            high=mid-1
            
    return minVal
    
    
arr=[3,4,5,1,2]
print(minNumber(arr,0,len(arr)-1))