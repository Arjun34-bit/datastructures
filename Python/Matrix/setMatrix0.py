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
    


def setZeroes(matrix):
    row = len(matrix)
    col = len(matrix[0])

    col0 = 1  # To check separately if first column needs to be zero

    # Step 1: Mark rows and columns
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                matrix[i][0] = 0  # Mark the row
                if j != 0:
                    matrix[0][j] = 0  # Mark the column
                else:
                    col0 = 0  # First column will need to be 0

    # Step 2: Set matrix[i][j] = 0 if either its row or column was marked
    for i in range(1, row):
        for j in range(1, col):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Step 3: Handle the first row
    if matrix[0][0] == 0:
        for j in range(col):
            matrix[0][j] = 0

    # Step 4: Handle the first column
    if col0 == 0:
        for i in range(row):
            matrix[i][0] = 0

    return matrix
   
mat=[[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
print(setZeroes(mat))