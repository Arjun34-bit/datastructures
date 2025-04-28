import math

class SmallestDivisor:
    def calculateThreshold(self,nums,divisor):
        currSum=0
        
        for i in range(0,len(nums)):
            currSum += math.ceil(nums[i]/divisor)
        return currSum
            


    def smallestDivisoriLinear(self,nums,threshold):
        low=min(nums)
        high=max(nums)
        
        for divisors in range(low,high+1):
            minThresh=self.calculateThreshold(nums,divisors)
            if minThresh<=threshold:
                return divisors
                
        return -1
    
    def smallestDivisorBinary(self,nums,threshold):
        low=min(nums)
        high=max(nums)
        
        while low<=high:
            mid=low+(high-low)//2
            
            if(self.calculateThreshold(nums,mid)<=threshold):
                high=mid-1
            else:
                low=mid+1
                
        return low


obj=SmallestDivisor()    
arr=[1,2,5,9]
threshold=6
print("Linear Search",obj.smallestDivisoriLinear(arr,threshold))    #O(N * N)
print("Binary Search",obj.smallestDivisorBinary(arr,threshold))     #O(N * log(max(nums)))