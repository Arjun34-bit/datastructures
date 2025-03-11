def hasTripletSum(arr, target):
    if(len(arr)<=1):
        return False

    arr.sort()
    
    for i in range(0,len(arr)-1):
        j=i+1
        k=len(arr)-1
        while j<k:
            sum=arr[i]+arr[j]+arr[k]
            
            if sum==target:
                return True
            elif sum>target:
                k-=1
            else:
                j+=1
                
    return False

print(hasTripletSum([1,4,45,6,10,8],24))