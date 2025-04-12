def minimum1(mat):
    row=len(mat)
    col=len(mat[0])
    
    index=0
    mini=col
    
    for i in range(0,row):
        count=0
        for j in range(0,col):
            if(mat[i][j]==1):
                count+=1
        if count<mini:
            mini=count
            index=i
    
    return index+1
    
    
mat=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(minimum1(mat))