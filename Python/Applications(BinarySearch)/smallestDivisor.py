import math

class LinearSearch:
    def calculateThreshold(self,nums,divisor):
        currSum=0
        
        for i in range(0,len(nums)):
            currSum += math.ceil(nums[i]/divisor)
        return currSum
            


    def smallestDivisor(self,nums,threshold):
        low=min(nums)
        high=max(nums)
        
        for divisors in range(low,high+1):
            minThresh=self.calculateThreshold(nums,divisors)
            if minThresh<=threshold:
                return divisors
                
        return -1


obj=LinearSearch()    
arr=[1,2,5,9]
threshold=6
print(obj.smallestDivisor(arr,threshold))