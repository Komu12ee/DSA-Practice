class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=len(matrix)
        cols=len(matrix[0])
        # Initialize a 3x3 matrix with zeros
        # rows, cols = 3, 3

        # BRUTE FORCE APPROCH 
        # temp = [[0 for _ in range(cols)] for _ in range(rows)]
        # print(temp)

        # for i in range(rows):
        #     for j in range(cols):
        #         temp[j][(rows-1)-i]=matrix[i][j]
        # for i in range(rows):
        #     for j in range(cols):
        #         matrix[i][j]=temp[i][j]
        

        # INPLACE APPROCH
        for i in range(rows):
            for j in range(i+1,cols):
                temp=matrix[j][i]
                matrix[j][i]=matrix[i][j]
                matrix[i][j]=temp
        for i in range(rows) :       
          self.rev(i,cols,matrix)

    def rev(self,i,cols,matrix):
        arr=[0]*cols
        for x in range(cols):
            arr[(cols-1)-x]=matrix[i][x]
        for x in range(cols):
            matrix[i][x]=arr[x]             
