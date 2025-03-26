class firstAndLast:
     
    def first(self,arr,x):
        low=0
        high=len(arr)-1
        f=-1
        
        while low<=high:
            mid=low+(high-low)//2
            
            if arr[mid]==x:
                f=mid
                high=mid-1
            elif arr[mid]<x:
                low=mid+1
            else:
                high=mid-1
        return f
        
    def last(self,arr,x):
        low=0
        high=len(arr)-1
        s=-1
        
        while low<=high:
            mid=low+(high-low)//2
            
            if arr[mid]==x:
                s=mid
                low=mid+1
            elif arr[mid]<x:
                low=mid+1
            else:
                high=mid-1
        return s
        
    def find(self, arr, x):
        
        # code here
        f=self.first(arr,x)
        s=self.last(arr,x)
        
        return [f,s]
    


arr=[1,3,5,5,5,5,8,123,125]
obj=firstAndLast()

result=obj.find(arr,5)

print(result)