class Solution:
    def allocatePainter(self,boards,painters):
        currPainter=1
        time=0
        
        n=len(boards)
        
        for painter in range(0,n):
            if (time+boards[painter] <= painters):
                time+=boards[painter]
            else:
                currPainter+=1
                time=boards[painter]
                
        return currPainter

    def minTime (self, arr, k):
        #code here
            
        if k==1:
            return sum(arr)
        
        low=max(arr)
        high=sum(arr)
        
        while low<=high:
            mid=low+(high-low)//2
            
            painterCount=self.allocatePainter(arr,mid)
            
            if painterCount > k:
                low=mid+1
            else:
                high=mid-1
        return low
    

obj=Solution()
boards=[5, 10, 30, 20, 15]
painters=3
print("Binary Search",obj.minTime(boards,painters))