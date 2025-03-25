def ceil(arr,x):

    low=0
    high=len(arr)-1
    obs=-1

    while low<=high:
        mid=low+(high-low)//2

        if arr[mid]<=x:
            obs=mid
            low=mid+1
        else:
            high=mid-1
    return obs




arr=[1,2,3,4,4,5,8,9]
print(ceil(arr,6))