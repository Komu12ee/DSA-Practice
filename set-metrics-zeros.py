class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        col=[0]*(len(matrix[0]))
        row=[0]*len(matrix)
        for i in range(len(row)):
            for j in range(len(col)):
                if matrix[i][j]==0:
                    col[j]=1
                    row[i]=1                                                            
        for i in range(len(row)):
            for j in range(len(col)):
                if(col[j] or row[i])   :
                    matrix[i][j]=0    
