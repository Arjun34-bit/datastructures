
# Brute Force Approach
def longestSubarray(arr, k):  
    count=0
    n=len(arr)
    
    for i in range(0,n-1):
        sums=0
        for j in range(i,n):
            sums+=arr[j]
            if sums==k:
                count=max(count,j-i+1)
    return count

arr=[10,5,2,7,1,-10]
print(longestSubarray(arr,15))



# Optimal Approach for negatives and zeros 
# Time Complexity : O(N)
# Space Complexity : O(N)
def longestSubarray(arr,k):
    maxLen=0
    hash_map={}
    n=len(arr)
    sums=0
    
    for i in range(0,n):
        sums+=arr[i]
        if(sums==k):
            maxLen=i+1
        rem=sums-k
        if rem in hash_map:
            lens=i-hash_map[rem]
            maxLen=max(maxLen,lens)
        if sums not in hash_map:
            hash_map[sums]=i
    return maxLen
    
    
    
arr=[10,5,2,7,1,-10]
print(longestSubarray(arr,15))