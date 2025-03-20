# Best Approach
def majorityElement(nums):

        n=len(nums)/2
        mp={}

        for i in range(0,len(nums)):
                mp[nums[i]]=mp.get(nums[i],0)+1
        for key, value in mp.items():
            if value>=n:
                return key
        
      
nums=[3,2,3]
print(majorityElement(nums))



# Optimal Approach not done 
def majorityElement(nums):

    n=len(nums)/2
    count=0
    el=0
    
    for i in range(0,len(nums)):
        if count==0:
            count=1
            el=nums[i]
        elif nums[i]==el:
            count+=1
        else:
            count-=1
    
    count1=0
    for j in range(0,len(nums)-1):
        if nums[j]==el:
            count1+=1

    if count>n:
        return el
    return -1