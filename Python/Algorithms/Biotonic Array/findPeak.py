def findPeak(arr):        
    if len(arr)==1:
        return 0
        
    low=1
    high=len(arr)-2
    
    if arr[0]>arr[low]:
        return 0
        
    if arr[len(arr)-1] > arr[high]:
        return len(arr)-1
        
    while low<=high:
        mid=low+(high-low)//2
        
        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return mid
        elif arr[mid]>arr[mid-1]:
            low=mid+1
        else:
            high=mid-1
    return -1


arr=[1,5,1,2,1]
print(findPeak(arr))