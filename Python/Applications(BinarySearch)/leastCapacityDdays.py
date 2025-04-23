class LinearSearch:
    def calculateLeast(self,prod,days,cap):
        currCap=0
        currDay=1

        for day in range(0,len(prod)):
            if currCap+prod[day]<=cap:
                currCap+=prod[day]
            else:
                currCap=prod[day]
                currDay+=1
        return currDay

    def weights(self,prod,d):
        low=max(prod)
        high=sum(prod)
        
        reqDays=high

        for capacity in range(low,high):
            reqDays=self.calculateLeast(prod,d,capacity)
            if reqDays<=d:
                return capacity
            
        return -1
    


class BinarySearch:
    def calculateLeast(self,prod,days,cap):
        currCap=0
        currDay=1

        for day in range(0,len(prod)):
            if currCap+prod[day]<=cap:
                currCap+=prod[day]
            else:
                currCap=prod[day]
                currDay+=1
        return currDay

    def weights(self,prod,d):
        low=max(prod)
        high=sum(prod)

        while low<=high:
            mid=low+(high-low)//2
            
            reqDays=self.calculateLeast(prod,d,mid)
            
            if reqDays<=d:
                high=mid-1
            else:
                low=mid+1
                
            
        return low
    




obj=LinearSearch()
obj1=BinarySearch()
arr=[1,2,1]
d=2
print("Linear Search",obj.weights(arr,d))
print("Binary Search",obj1.weights(arr,d))