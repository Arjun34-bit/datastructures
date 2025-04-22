class LinearSearch:
    def calculateMinDays(self,bloomDays,bouquets,flowers,day):
        n=len(bloomDays)
        adjFlowers=0
        nBouquets=0
        
        for blooms in range(0,n):
            if bloomDays[blooms]<=day:
                adjFlowers+=1
            else:
                nBouquets+=(adjFlowers//flowers)
                adjFlowers=0
            
        nBouquets+=adjFlowers//flowers    
        if(nBouquets>=bouquets):
            return True
        else:
            return False



    def bloom(self,bloomDay,bouquets,flowers):
        low=min(bloomDay)
        high=max(bloomDay)
                
        for days in range(low,high+1):
            if(self.calculateMinDays(bloomDay,bouquets,flowers,days)):
                return days
            
        return -1


class BinarySearch:
    def calculateMinDays(self,bloomDays,bouquets,flowers,day):
        n=len(bloomDays)
        adjFlowers=0
        nBouquets=0
        
        for blooms in range(0,n):
            if bloomDays[blooms]<=day:
                adjFlowers+=1
            else:
                nBouquets+=adjFlowers//flowers
                adjFlowers=0
            
        nBouquets+=adjFlowers//flowers    
        if(nBouquets>=bouquets):
            return True
        else:
            return False
        
    def bloom(self,bloomDay,bouquets,flowers):
        low=min(bloomDay)
        high=max(bloomDay)

        ans=high
                
        
        while low<=high:
            mid=low+(high-low)//2
            
            if(self.calculateMinDays(bloomDay,bouquets,flowers,mid)):
                ans=mid
                high=mid-1
            else:
                low=mid+1
                
        return ans


obj=LinearSearch()  #Time Complexity is O(min - max + 1) * O(n)  for worst case

obj1=BinarySearch()  #Time Complexity is O(log2(min - max + 1)) * O(n)  for worst case

bloomD=[1,10,3,10,2]
m=3
k=1
print("Linear Search",obj.bloom(bloomD,m,k))
print("Binary Search",obj1.bloom(bloomD,m,k))
        
        