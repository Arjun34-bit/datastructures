def binarySearch(arr,target):
    
    low=0
    high=len(arr)-1
    
    print(arr)
    
    while low<=high:
        mid=low+(high-low)//2
        
        if arr[mid]==target:
            return True
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return False
    
    
def search2D(arr,target):
    col=len(arr[0])-1
    
    searchVal=False
    
    for i in range(0,len(arr)):
        if arr[i][0]<=target and target<=arr[i][col]:
            searchVal=binarySearch(arr[i],target)
        else:
            continue
        
    return searchVal
    
    
arr=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(search2D(arr,30))