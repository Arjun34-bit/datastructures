class Solution:
    def split(self,arr,subSum,N,K):
        split=1
        subArrSum=0
        
        for num in arr:
            if subArrSum + num > subSum:
                split+=1
                subArrSum=num
                
                if split > K:
                    return False
                    
            else:
                subArrSum+=num
                
        return True 
    
    def splitArray(self, arr, N, K):
        # code here 
        low=max(arr)
        high=sum(arr)
        
        result=high
        
        while low<=high:
            mid=low+(high-low)//2
            
            if self.split(arr,mid,N,K):
                result=mid
                high=mid-1
            else:
                low=mid+1
        return result
    




obj=Solution()
arr=[1,2,3,4]
K=3
N=4
print("Binary Search",obj.splitArray(arr,N,K))