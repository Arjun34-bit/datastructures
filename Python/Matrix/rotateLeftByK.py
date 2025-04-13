def reverse(arr,k):
    n=len(arr)
        
    l=0
    r=n-1
    
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
        
    l=0
    right=n-k
    while l<right:
        arr[l],arr[right]=arr[right],arr[l]
        l+=1
        right-=1
        
    l=n-k+1
    r=n-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
        
    return arr

def rotateByK(mat,k):
    row=len(mat)
    col=len(mat[0])
    
    
    low=0
    right=row-1
    
    k=k%col
    
    while low<=right:
        reverse(mat[low],k+1)
        low+=1
        return mat
    
    
    
    
mat=[[1,2,3],[4,5,6],[7,8,9]]
print(rotateByK(mat,1))