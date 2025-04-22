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
    


obj=LinearSearch()
arr=[1,2,1]
d=2
print(obj.weights(arr,d))