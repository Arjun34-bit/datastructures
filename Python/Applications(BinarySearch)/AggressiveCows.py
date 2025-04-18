#Linear Search Approach




class LinearApproach():
    def canWePlaceCows(self,arr,dis,cows):
        cowCount=1
        last=arr[0]

        for i in range(1,len(arr)-1):
            if(arr[i]-last >= dis):
                cowCount+=1
                last=arr[i]

            if(cowCount >= cows):
                return True


    def aggressiveCows(self,arr,cows):
        n=arr[-1]-arr[0]


        for i in range(1,n):
            if not self.canWePlaceCows(arr,i,cows):
                return i-1
            
        return n
    



obj=LinearApproach()
stalls=[1,2,4,8,9]
cows=3
print(obj.aggressiveCows(stalls,cows))