def setMatrix0(mat):
    
    row=len(mat)
    col=len(mat[0])
    
    r=[0]*row
    c=[0]*col
    
    for i in range(0,row):
        for j in range(0,col):
            if mat[i][j]==0:
                r[i]=1
                c[j]=1
            else:
                continue
            
    for i in range(0,row):
        for j in range(0,col):
            if r[i]==1 or c[j]==1:
                mat[i][j]=mat[i][j]*0
            else:
                continue
                
                
    return mat
    
    
    
mat=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(setMatrix0(mat))