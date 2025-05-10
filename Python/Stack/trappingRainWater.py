def maxWater(arr):        
    l=0
    r=len(arr)-1
    
    leftMax=0
    rightMax=0
    
    res=0
    
    while l<=r:
        if arr[l] <= arr[r]:
            if arr[l] >= leftMax:
                leftMax=arr[l]
            else:
                res+=leftMax - arr[l]
                
            l+=1
                
        else:
            if arr[r] >= rightMax:
                rightMax=arr[r]
            else:
                res+=rightMax - arr[r]
            r-=1
            
    return res