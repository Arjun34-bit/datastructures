import sys

def maxVal(arr,low,high):

    maxVals=-sys.maxsize-1

    while low<=high:

        mid=low+(high-low)//2

        if arr[low]<=arr[mid]:
            maxVals=max(maxVals,arr[mid])
            low=mid+1
        else:
            maxVals=max(maxVals,arr[high])
            high=mid-1
    return maxVals




arr=[10,50,40,30,20]
print(maxVal(arr,0,len(arr)-1))