def insert(n,x,st):
    st.append(x)
    l=0
    r=len(st)-1
    
    while l<r:
        st[l],st[r]=st[r],st[l]
        l+=1
        r-=1
        
        
    l1=1
    r1=len(st)-1
    
    while l1<r1:
        st[l1],st[r1]=st[r1],st[l1]
        l1+=1
        r1-=1
        
        
    return st
        
    
st=[4,3,2,1,8]
print(insert(5,2,st))