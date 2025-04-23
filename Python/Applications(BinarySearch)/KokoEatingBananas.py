import math

class BinarySearch:
    def calculateSpeed(piles,speed):
        currHour=0
        
        for i in range(0,len(piles)):
            currHour+=math.ceil(piles[i]/speed)
        
        return currHour
    
    def bananas1(piles,h):
        low=1
        high=max(piles)
        
        speed=high
        
        for speed in range(low,high):
            reqHour=self.calculateSpeed(piles,speed)
            if reqHour<=h:
                return speed
                
        return speed

    



class BinarySearch:
    def calculateSpeed(piles,speed):
        currHour=0
        
        for i in range(0,len(piles)):
            currHour+=math.ceil(piles[i]/speed)
        
        return currHour
    
    def bananas(piles,h):
        low=1
        high=max(piles)
        
        ans=high
        
        while low<=high:
            mid=low+(high-low)//2
            
            reqHours=self.calculateSpeed(piles,mid)
            
            if reqHours<=h:
                high=mid-1
                ans=mid
            else:
                low=mid+1
                
        return low
    



    
    
arr=[30,11,23,4,20]
h=5
print(bananas(arr,h))
        
    