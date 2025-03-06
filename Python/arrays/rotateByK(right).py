class Rotate:
    def __init__(self,arr):
        self.arr=arr
    def reverse(self,l,r):
        while l<r:
            self.arr[l],self.arr[r]=self.arr[r],self.arr[l]
            l=l+1
            r=r-1
    def rotate(self):
        l=0
        n=len(arr)
        temp=0
        self.reverse(0,n-1)
        self.reverse(0,0)
        self.reverse(1,n-1)
        return self.arr
    

arr=[1,2,3,4,5]
r=Rotate([1,2,3,4,5])
print(r.rotate())

# Time Complexity is O(2N) 
# Space Complexity is O(1)