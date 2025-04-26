def calculatePair(arr,minAns):
    pairs=0
    j=0
    
    
    for i in range(0,len(arr)):
        while (arr[i]-arr[j])>minAns:
            j+=1
        pairs += i - j
                
    return pairs


def smallestPair(arr,k):
    
    arr.sort()
    
    low=0
    high=arr[-1] - arr[0]
    
    while low<=high:
        mid=low+(high-low)//2
        
        if(calculatePair(arr,mid)>=k):
            high=mid-1
        else:
            low=mid+1
    return low
    
    
arr=[1,6,1]
k=3
print(smallestPair(arr,k))