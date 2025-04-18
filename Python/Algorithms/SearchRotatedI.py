
# Time Complexity O(LOGN)
def search(arr, target):
    low=0
    high=len(arr)-1

    while low<=high:
        mid=low+(high-low)//2

        if arr[mid]==target:
            return mid
        if arr[low]<=arr[mid]:
            if arr[low]<=target and target<=arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<=target and target<=arr[high]:
                low=mid+1
            else:
                high=mid-1
    return -1



arr=[4,5,6,7,0,1,2]
print(search(arr,1))