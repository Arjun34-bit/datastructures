import sys

def maxVal(arr,low,high):

    maxVals=-sys.maxsize-1

    idx=0

    while low<=high:

        mid=low+(high-low)//2

        if arr[low]<=arr[mid]:
            maxVals=max(maxVals,arr[mid])
            idx=mid
            low=mid+1
        else:
            maxVals=max(maxVals,arr[high])
            idx=high
            high=mid-1
    return [idx,maxVals]




arr=[6, 9, 2, 4]
print(maxVal(arr,0,len(arr)-1))