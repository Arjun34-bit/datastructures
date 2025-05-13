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
    
    
arr=[60, 20, 50, 40, 10, 50, 60]
print(largestArea(arr))