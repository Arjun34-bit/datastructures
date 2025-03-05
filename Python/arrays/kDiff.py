def kDifference(arr,target):
    left=0
    right=1

    while right<len(arr)-1:
        diff=arr[right]-arr[left]

        if(diff==target):
            return (arr[left],arr[right])
        elif(diff<target):
            right+=1
        else:
            left+=1
        
        if(left==right):
            right+=1
    return []


print(kDifference([1, 3, 5, 7, 9],4))