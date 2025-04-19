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
    



class BinaryAppraoch():
    def canWePlaceCows(self,arr,dis,cows):
        cowCount=1
        last=arr[0]

        for i in range(1,len(arr)):
            if(arr[i]-last >= dis):
                cowCount+=1
                last=arr[i]

            if(cowCount >= cows):
                return True


    def aggressiveCows(self,arr,k):
        low=1
        high=arr[-1]-arr[0]

        while low<=high:
            mid=low+(high-low)//2

            if (self.canWePlaceCows(arr,mid,k)):
                low=mid+1
            else:
                high=mid-1
        return high
            



obj=LinearApproach()
obj1=BinaryAppraoch()

stalls=[1,2,4,8,9]
cows=3
print("Linear Approach ",obj.aggressiveCows(stalls,cows))
print("Binary Approach ",obj1.aggressiveCows(stalls,cows))