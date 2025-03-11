
# Better Approach
# Time Complexity is O(N)
# Space Complexity is O(N)
def twoSum(arr,target):
    if(len(arr)<=1):
        return False
    
    hash_map={}
    for i in range(0,len(arr)):
        rem=target-arr[i]
        if rem in hash_map:
            return True
        else:
            hash_map[arr[i]]=arr[i]
    return False
    
    
arr=[1,2,3,4,5,6]
print(twoSum(arr,11))




def twoPointer(nums,target):
    left=0
    right=len(nums)-1
    result=[]
    while left<right:
        total=nums[left]+nums[right]
        
        if(total==target):
            result.append([left,right])
            left+=1
            right-=1
        elif(total<target):
            left+=1
        else:
            right-=1
    return result

# print(twoPointer([1,2,3,4,5,6,7,8,9],10))