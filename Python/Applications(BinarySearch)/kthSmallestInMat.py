class Solution(object):
    def lessThanK(self,el,n,m):
        sums=0
        
        for i in range(1,m+1):
            sums+=min(el//i,n)
        
        return sums

    def findKthNumber(self, m, n, k):
        low=1
        high=m*n
        
        while low<=high:
            mid=low+(high-low)//2
            
            if(self.lessThanK(mid,n,m)<k):
                low=mid+1
            else:
                high=mid-1
                
        return low
    


obj=Solution()
m=3
n=3
k=3
print(obj.findKthNumber(m,n,k))