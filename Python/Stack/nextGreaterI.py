def nextGreaterEl(arr):
    n=len(arr)
    if len(arr)<=1:
        return [-1]
        
    nge=[-1] * n
    
    st=[]
        
    for i in range(n-1,-1,-1):
        
        while (st and st[-1] <= arr[i]):
            print("rm")
            st.pop()
            
        if i<n:
            if len(st)!=0:
                nge[i]=st[-1]
            else:
                nge[i]=-1
                
        st.append(arr[i])
        
    return nge
        
        
arr=[1,3,2,4]
print(nextGreaterEl(arr))    #  TC:O(2n + 2n)  ~ TIME COMPLEXITY:O(n)  and SPACE COMPLEXITY:O(n)