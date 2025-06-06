class Solution(object):
    def findMaxRowindex(self,mat,n,m,mid):
        maxEl=-1
        index=-1

        for i in range(0,n):
            if(mat[i][mid]>maxEl):
                maxEl=mat[i][mid]
                index=i
        
        return index


    def findPeakGrid(self, mat):
        n=len(mat)
        m=len(mat[0])
        low=0
        high=m-1

        while low<=high:
            mid=low+(high-low)//2

            maxRowIndex=self.findMaxRowindex(mat,n,m,mid)

            if mid-1>=0:
                left=mat[maxRowIndex][mid-1]
            else:
                left=-1

            if mid+1<m:
                right=mat[maxRowIndex][mid+1]
            else:
                right=-1

            if(mat[maxRowIndex][mid] > left and mat[maxRowIndex][mid]>right):
                return [maxRowIndex,mid]
            elif (mat[maxRowIndex][mid]<left):
                high=mid-1
            else:
                low=mid+1
        return [-1,-1]


obj=Solution()

mat=[[1,2,3],[5,4,6],[4,5,3]]
print(obj.findPeakGrid(mat))