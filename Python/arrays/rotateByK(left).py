def rotateArray(arr: list, k: int) -> list:
    print("Initial Array",arr)
    n=len(arr)-1
    l,r=0,len(arr)-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    print("1st Reverse",arr)
    l,r=0,n-k
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    print("2nd Reverse",arr)
    l,r=n-k+1,n
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    print("3rd Reverse",arr)
        
    return arr
    
print(rotateArray([1 ,3, 6, 11, 12, 17],4))

# Time Complexity is O(2N) 
# Space Complexity is O(1)