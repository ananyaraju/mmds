import math
max = 100

def cholesky(matrix, n) :
    lower = [[0 for x in range(n+1)]
                for y in range (n+1)]
    for i in range (n) :
        for j in range (i+1) :
            sum1 = 0
            if (i==j) :
                for k in range(j) :
                    sum1 += pow (lower[j][k], 2)
                lower[j][i] = int(math.sqrt(abs(matrix[j][i] - sum1)))
            else :
                for k in range (j) :
                    sum1 += (lower[i][k]*lower[j][k])
                if (lower[j][j] > 0) :
                    lower[i][j] = int((matrix[i][j] - sum1)/lower[j][j])
    print ("Lower Triangular Matrix: ")
    for i in range (n) :
        for j in range (n) :
            print(lower[i][j], end='\t')
        print()
    print()
    print("Transpose Matrix: ")
    for i in range(n) :
        for j in range(n) :
            print (lower[j][i], end='\t')
        print()

n = 3
matrix = [ 
 [6,18,3], 
 [2,12,1], 
 [4,15,3] 
] 
 
cholesky(matrix, n)
