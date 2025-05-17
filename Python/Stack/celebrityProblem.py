def knows(a,b,mat):
    if(mat[a][b] == 1):
        return True
    else:
        return False
def celebrity(mat):

    n=len(mat)

    st=[]
    
    for i in range(0,n):
        st.append(i)
        
    while len(st) > 1:
        a=st[-1]
        st.pop()
        
        b=st[-1]
        st.pop()
        
        if(knows(a,b,mat)):
            st.append(b)
        else:
            st.append(a)
            
    celebrity=st[-1]
    
    
    isRow=False
    zeroCount=0
    
    for i in range(0,n):
        if(mat[celebrity][i] == 0):
            zeroCount+=1
            
    if zeroCount == n-1:
        isRow=True
    
    isCol=False
    oneCount=0
    
    for j in range(0,n):
        if(mat[j][celebrity] == 1):
            oneCount+=1
            
    if oneCount == n:
        isCol=True
        
    if isRow and isCol:
        return celebrity
    else:
        return -1
        
        
mat=[[1, 1, 0], [0, 1, 0], [0, 1, 1]]
print(celebrity(mat))