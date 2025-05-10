def nextSmallerEl( arr, n):
    if n<=1:
        return [-1]
        
    nse=[-1] * n
    
    st=[]
        
    for i in range(n-1,-1,-1):
        
        while (st and st[-1] >= arr[i]):
            st.pop()
            
        if i<n:
            if len(st)!=0:
                nse[i]=st[-1]
            else:
                nse[i]=-1
                
        st.append(arr[i])
        
    return nse


arr=[100,80,60,70,60,75,85]
print(nextSmallerEl(arr,len(arr)))