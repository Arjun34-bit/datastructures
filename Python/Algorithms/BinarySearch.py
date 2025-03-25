def binarySearch(arr,k):

    low=0
    high=len(arr)-1

    while low<=high:

        mid=low+(high-low)//2

        if arr[mid]==k:
            return True
        elif arr[mid]>k:
            high=mid-1
        else:
            low=mid+1
    return False




arr=[1,2,5,7,8,9,10,15]
print(binarySearch(arr,10))