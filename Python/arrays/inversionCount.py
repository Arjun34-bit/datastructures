# Brute Force Approach
# Time Complexity: O(N^2)
# Space Compleity : O(1)

def inversionCount(arr):
    n=len(arr)
    count=0
    
    for i in range(0,n-1):
        for j in range(i+1,n):
            if arr[i]>arr[j] and i<j:
                count+=1
    
    return count
       
arr=[2, 3, 4, 5, 6]
print(inversionCount(arr))