import numpy as np

r = int(input("Number of rows in matrix: "))
c = int(input("Number of cols in matrix: "))

if (r!=c):
    print("only square matrices are valid\n")
else:
    m = []
    print("\nenter matrix data")
    for x in range(r):
        col = []
        for y in range(c):            
            val = int(input("data: "))
            col.append(val)
        m.append(col)
    print("\nmatrix: ")
    print(m)

    rank = np.linalg.matrix_rank(m)
    print("rank of matrix = ",rank)