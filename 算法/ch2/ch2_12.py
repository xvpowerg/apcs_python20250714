def printMatrix(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            print(matrix[r][c],end = " ")
        print()
def matrixAdd(A,B):
    n = len(A)
    m = len(A[0])
    c = [[0] * m for row in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = A[i][j] + B[i][j]
    return c


matrixA = [[1,3,5],
           [7,9,11],
           [13,15,17]]
matrixB = [[9,8,7],
           [6,5,4],
           [3,2,1]]
c = matrixAdd(matrixA,matrixB)
printMatrix(c)
