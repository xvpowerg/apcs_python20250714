def printMatrix(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            print(matrix[r][c],end = " ")
        print()

def matrixMutiply(A,B):
    m = len(A)
    na = len(A[0])
    nb = len(B)
    p = len(B[0])
    if na != nb:
        print("AB無法相乘")
        return
    c = [[0]* p for row in range(m)]
    for i in range(m):
        for j in range(p):
            tmp = 0
            for k in range(na):
                tmp += A[i][k] * B[k][j]
            c[i][j] = tmp
    return c           
matrixA = [[6,3,5], [8,9,7]]
matrixB = [[5,10], [14,7], [6,8]]
m = matrixMutiply(matrixA,matrixB)
printMatrix(m)

