def stockSpan(arr):        
    span=1
    st=[]
    
    result=[]
    
    for i in range(0,len(arr)):
        span=1
        while st and st[-1][0] <= arr[i]:
            span += st[-1][1]
            st.pop()
        result.append(span)
        st.append([arr[i],span])
        
    return result
    
    
arr=[100,80,60,70,60,75,85]
print(stockSpan(arr))