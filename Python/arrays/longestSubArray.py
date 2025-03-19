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
# prefix with hash aprroach 
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



# Optimal Approach for arrays with positive numbers only
# Two Pointer Approach
# # Time Complexity : O(2N)
# Space Complexity : O(N) 
def longestSubArray(arr,k):
    maxLen=0
    i=0
    j=0
    sums=arr[0]
    n=len(arr)
    
    while j<n:
        while i<=j and  sums>k:
            sums=sums-arr[i]
            i+=1
        if sums==k:
            maxLen=max(maxLen,j-i+1)
        j+=1
        if(j<n):
            sums+=arr[j]
    return maxLen


arr=[1,2,3,1,1,1,1]
print(longestSubArray(arr,3))
    