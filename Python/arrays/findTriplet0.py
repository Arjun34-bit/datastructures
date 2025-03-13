def findTriplets(arr):
    n=len(arr)
    
    arr.sort()
    
    for i in range(n-1):
        left=i+1
        right=n-1
        while left<right:
            sums=arr[i]+arr[left]+arr[right]
            
            if sums==0:
                return True
            elif sums>0:
                right-=1
            else:
                left+=1
    return False

arr=[0, -1, 2, -3, 1]
print(findTriplets(arr))