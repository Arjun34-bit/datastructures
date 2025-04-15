def findPeak(arr):
        low=0
        high=len(arr)-1

        maxVal=-100
        idx=0
        
        # print(arr)

        while low<=high:
            mid=low+(high-low)//2

            if arr[mid] > maxVal:
                maxVal = arr[mid]
                idx = mid

            if arr[low] <= arr[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return [idx,maxVal]

def findPeakGrid(mat):
    row=len(mat)
    col=len(mat[0])-1

    colNum=0
    rowNum=0

    maxNum=0
    result=0
    for i in range(0,row):
        idx,val=findPeak(mat[i])
        print(maxNum)
        if result<val:
            result=val
            rowNum=i
            colNum=idx

    return [rowNum,colNum]
    
    
mat=[[10,50,40,30,20],[1,500,2,3,4]]
print(findPeakGrid(mat))