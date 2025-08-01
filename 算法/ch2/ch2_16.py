def printMatrix(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            print(matrix[r][c],end = " ")
        print()

def rotate(matrixA):
    matrixB = []
    r = len(matrixA)
    c = len(matrixA[0])
    for i in range(c):
        row =[] 
        for j in range(r-1,-1,-1):
            row.append(matrixA[j][i])    
        matrixB.append(row)
    return matrixB     
            
m1 = [[3,6],
      [2,5],
      [1,4]]
m2  = rotate(m1)
printMatrix(m1)
print("旋轉~")
printMatrix(m2)
