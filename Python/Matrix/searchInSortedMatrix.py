def binarySearch(arr,target):
    low=0
    high=len(arr)-1
    
    while low<=high:
        mid=low+(high-low)//2
        
        if arr[mid]==target:
            return True
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return False
    

def searchMatrix(mat, x):
    row=len(mat)
    result=0
    for i in range(0,row):
        if result==True:
            break
        result=binarySearch(mat[i],x)
        
    return result
	
	
	
mat=[[18 ,21, 27, 38, 55, 67]]
print(searchMatrix(mat,55))