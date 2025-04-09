#Time Complexity is O(m + logn)

class searchMatrix1:
    def binarySearch(self,arr,target):
        
        low=0
        high=len(arr)-1
        
        
        while low<=high:
            mid=low+(high-low)//2
            
            if arr[mid]==target:
                return True
            elif arr[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return False
        
        
    def search2D(self,arr,target):
        col=len(arr[0])-1
        
        searchVal=False
        
        for i in range(0,len(arr)):
            if arr[i][0]<=target and target<=arr[i][col]:
                searchVal=self.binarySearch(arr[i],target)
            else:
                continue
            
        return searchVal
    


class searchMatrix2:
    def search(self,arr,target):


        rows=len(arr)
        cols=len(arr[0])

        low=0
        high=rows*cols-1

        while low<=high:
            mid=low+(high-low)//2
            row=mid//cols
            col=mid%cols

            if arr[row][col]==target:
                return True
            elif arr[row][col]<target:
                low=mid+1
            else:
                high=mid-1
        return False
    

obj=searchMatrix1()
obj1=searchMatrix2()

arr=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]

print(obj.search2D(arr,16))
print(obj1.search(arr,16))