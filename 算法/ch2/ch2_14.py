def printMatrix(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            print(matrix[r][c],end = " ")
        print()
        
matrixA = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12]]

def matrixT(A):
    m = len(A)
    n = len(A[0])
    B = [[0] * m for row in range(n)]
    for i in range(n):
        for j in range(m):
            B[i][j] = A[j][i]
    return B            

matrixB =  matrixT(matrixA)
print("A:")
printMatrix(matrixA)
print("B:")
printMatrix(matrixB)
