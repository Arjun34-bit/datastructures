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

print(twoPointer([1,2,3,4,5,6,7,8,9],10))