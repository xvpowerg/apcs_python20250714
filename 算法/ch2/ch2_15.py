def printMatrix(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            print(matrix[r][c],end = " ")
        print()
def flip(matrixA):
    matrixB = []
    r = len(matrixA)
    for i in range(r-1,-1,-1):
        matrixB.append(matrixA[i])
    return matrixB

m1 = [[1,4],
      [2,5],
      [3,6]]
m2 = flip(m1)
printMatrix(m1)
print("翻轉後")
printMatrix(m2)
