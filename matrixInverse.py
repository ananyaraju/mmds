order = int(input("Order of matrix: ")) 
matrix = [[0 for i in range(order * 2)] for j in range(order)] 
print("Enter the matrix row-wise, with each element seperated by spaces:") 
for i in range(order): 
    matrix[i] = [int(x) for x in input().split(" ")] + [0]*order 
 
for i in range(order): 
    for j in range(order): 
        if i == j: 
            matrix[i][j+order] = 1
 
for i in range(order): 
    if matrix[i][i] == 0: 
        exit(0) 
    for j in range(order): 
        if i!=j: 
            ratio = matrix[j][i] / matrix[i][i] 
            for k in range(2*order): 
                matrix[j][k] = matrix[j][k] - ratio * matrix[i][k] 
 
for i in range(order): 
    divisor = matrix[i][i] 
    for j in range(2*order): 
        matrix[i][j] = matrix[i][j]/divisor 
 
print(len(matrix))

