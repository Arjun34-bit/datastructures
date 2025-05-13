def largestArea(arr):
    n=len(arr)
    leftSmall=[0]*n
    rightSmall=[0]*n
    
    st=[]
    
    result=0
    
    for i in range(0,n):
        while st and arr[st[-1]] >= arr[i]:
            st.pop()
            

        if len(st) != 0:
            leftSmall[i]=st[-1] + 1
        else:
            leftSmall[i]=0
                
        st.append(i)
        
        
        
    while len(st) != 0:
        st.pop()
        
    for j in range(n-1,-1,-1):
        while st and arr[st[-1]] >= arr[j]:
            st.pop()
            
        if len(st) != 0:
            rightSmall[j]=st[-1] - 1
        else:
            rightSmall[j]=n-1
                
        st.append(j)

        
    for i in range(0,n):
        maxArea=(rightSmall[i] - leftSmall[i] + 1) * arr[i]
        result=max(result,maxArea)
        
    return result


def largestAreaInMatrix(arr):
    heights=[0]*len(arr[0])
    maxArea=0
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            if arr[i][j] == 1:
                heights[j] += 1
            else:
                heights[j] = 0

        area=largestArea(heights)
        maxArea=max(maxArea,area)

    return maxArea

    
    
arr=[[0, 1, 1, 0],[1, 1, 1, 1],[1, 1, 1, 1],[1, 1, 0, 0]]


print(largestAreaInMatrix(arr))