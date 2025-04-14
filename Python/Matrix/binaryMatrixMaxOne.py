def binarySearch(arr,target):
        low=0
        high=len(arr)-1
        
        f=-1
        
        while low<=high:
            mid=low+(high-low)//2
            if arr[mid]==target:
                f=mid
                high=mid-1
            elif arr[mid]<target:
                low=mid+1
            else:
                high=mid-1
        if(f==-1):
            return 0
        else:
            return len(arr)-f
            
            
def findMaxRow(mat, N):
    
    index=0
    val=0
    maxCount=-1
    
    for i in range(0,N):
        val=binarySearch(mat[i],1)
        
        if maxCount<=val:
            if val==maxCount and index<i:
                continue
            index=i
            maxCount=val
            
    return index,maxCount
    
    
    
mat=[[0, 0, 1],[0, 1, 1],[0, 0, 0]]
print(findMaxRow(mat,3))

