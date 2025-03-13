def fourSum( arr, target):
    arr.sort()
    n=len(arr)
    result=[]
    
    for i in range(0,n-3):
        if i>0 and arr[i]==arr[i-1]:
            continue
        for j in range(i+1,n-2):
            if j>i+1 and arr[j]==arr[j-1]:
                continue
            left=j+1
            right=n-1
            while left<right:
                sums=arr[i]+arr[j]+arr[left]+arr[right]
                
                if sums==target:
                    result.append([arr[i],arr[j],arr[left],arr[right]])
                    
                    while left<right and arr[left]==arr[left+1]:
                        left+=1
                    while left<right and arr[right]==arr[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif sums<target:
                    left+=1
                else:
                    right-=1
    return result


arr=[0, 0, 2, 1, 1]
print(fourSum(arr,3))