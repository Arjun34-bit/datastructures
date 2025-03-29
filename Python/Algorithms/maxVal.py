def maxVal(arr,low,high):

    index=0

    while low<=high:

        mid=low+(high-low)//2

        if arr[low]<=arr[mid]:
            index=mid
            low=mid+1
        else:
            index=high
            high=mid-1
    return index




arr=[6, 9, 2, 4]
print(maxVal(arr,0,len(arr)-1))