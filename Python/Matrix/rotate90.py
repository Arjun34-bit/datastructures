def rotateby90(matrix): 
    n=len(matrix)

    result = [[None for _ in range(n)] for _ in range(n)]
    
    for i in range(0,n):
        for j in range(0,n):
            result[(n-1)-j][i]=matrix[i][j]
            
            
    return result




class Solution:
    
    def transpose(self,matrix):
        n=len(matrix)
    
        for i in range(0,n-1):
            for j in range(i+1,n):
                temp=matrix[j][i]
                matrix[j][i]=matrix[i][j]
                matrix[i][j]=temp
        return matrix
    
    
    def rotateby90(self, mat): 
        # code here
        self.transpose(mat)
        l=0
        r=len(matrix)-1
        
        while l<r:
            mat[l],mat[r]=mat[r],mat[l]
            l+=1
            r-=1
            
        return mat